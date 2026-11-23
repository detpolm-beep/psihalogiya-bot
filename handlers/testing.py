"""Test jarayoni handler'lari: tanlash, javob berish, natija."""

from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.tests import DISCLAIMER, TESTS, get_result_text, max_score
from keyboards import question_kb, result_kb, tests_menu_kb
from states import TestingStates
import db

router = Router(name="testing")


@router.callback_query(F.data.startswith("select:"))
async def cb_select(call: CallbackQuery, state: FSMContext):
    """Testni boshlash (yoki qayta boshlash)."""
    test_id = call.data.split(":", 1)[1]
    test = TESTS.get(test_id)
    if not test:
        await call.answer("Test topilmadi.", show_alert=True)
        return

    questions = test["questions"]
    await state.set_state(TestingStates.in_test)
    await state.update_data(test_id=test_id, q_index=0, score=0, answers=[])

    first = questions[0]
    await call.message.edit_text(
        f"📋 <b>{test['title']}</b>\n\n"
        f"{test['description']}\n\n"
        f"<b>Savol 1 / {len(questions)}</b>\n{first['text']}",
        reply_markup=question_kb(first["options"]),
    )
    await call.answer()


@router.callback_query(StateFilter(TestingStates.in_test),
                        F.data.startswith("ans:"))
async def cb_answer(call: CallbackQuery, state: FSMContext):
    """Javobni qayd etish va keyingi savolga o'tish yoki natijani chiqarish."""
    data = await state.get_data()
    test_id = data["test_id"]
    q_index = data["q_index"]
    score = data["score"]
    answers = data["answers"]

    test = TESTS[test_id]
    questions = test["questions"]

    option_index = int(call.data.split(":", 1)[1])
    if option_index < 0 or option_index >= len(questions[q_index]["options"]):
        await call.answer("Noto'g'ri javob.", show_alert=True)
        return

    chosen = questions[q_index]["options"][option_index]
    score += chosen["score"]
    answers.append(chosen["score"])
    q_index += 1

    if q_index < len(questions):
        await state.update_data(q_index=q_index, score=score, answers=answers)
        next_q = questions[q_index]
        await call.message.edit_text(
            f"📋 <b>{test['title']}</b>\n\n"
            f"<b>Savol {q_index + 1} / {len(questions)}</b>\n"
            f"{next_q['text']}",
            reply_markup=question_kb(next_q["options"]),
        )
    else:
        await state.clear()
        result_text = get_result_text(test, score)
        # Agar depressiya testining oxirgi (o'ziga zarar) savoliga
        # ijobiy javob berilgan bo'lsa, krizis eslatmasini qo'shamiz.
        if "crisis_note" in test and answers and answers[-1] > 0:
            result_text += "\n\n" + test["crisis_note"]

        # Natijani bazaga yozib qo'yamiz (admin statistikasi uchun)
        await db.log_test_result(call.from_user.id, test_id, score)

        await call.message.edit_text(
            f"🏁 <b>Test yakunlandi</b>\n\n"
            f"📋 {test['title']}\n"
            f"📊 Natija: <b>{score} / {max_score(test)}</b>\n\n"
            f"{result_text}\n\n{DISCLAIMER}",
            reply_markup=result_kb(test_id),
        )
    await call.answer()


@router.callback_query(F.data == "cancel")
async def cb_cancel(call: CallbackQuery, state: FSMContext):
    """Testni to'xtatish (inline tugma orqali)."""
    await state.clear()
    await call.message.edit_text(
        "Test to'xtatildi. 🛑",
        reply_markup=tests_menu_kb(),
    )
    await call.answer()


@router.callback_query()
async def cb_fallback(call: CallbackQuery):
    """Tutilib qolmagan (eskirgan) tugmalarni "yopish"."""
    await call.answer(
        "Bu tugma endi amalda emas. Iltimos, /start orqali boshlang.",
        show_alert=True,
    )
