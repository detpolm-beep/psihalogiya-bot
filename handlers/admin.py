"""Admin panel: statistika, foydalanuvchilar, broadcast, bot haqida."""

from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import ADMIN_IDS
from data.tests import TESTS
from keyboards import admin_menu_kb
from states import AdminStates
import db

router = Router(name="admin")


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


ADMIN_MENU_TEXT = (
    "🔧 <b>Admin panel</b>\n\nKerakli bo'limni tanlang:"
)


@router.message(Command("admin"))
async def cmd_admin(message: Message, state: FSMContext):
    uid = message.from_user.id
    if not ADMIN_IDS:
        # Admin'lar sozlanmagan — foydalanuvchiga o'z ID'sini ko'rsatamiz
        await message.answer(
            "🔧 Admin panel hozircha o'chirilgan — .env da <b>ADMIN_IDS</b> "
            "sozlanmagan.\n\n"
            f"Sizning Telegram ID'ingiz: <code>{uid}</code>\n\n"
            "Uni .env fayliga shu ko'rinishda qo'shing:\n"
            "<code>ADMIN_IDS=123456789</code>\n"
            "so'ng botni qayta ishga tushiring."
        )
        return
    if not is_admin(uid):
        await message.answer("🚫 Ushbu panel faqat admin'lar uchun.")
        return
    await state.clear()
    await message.answer(ADMIN_MENU_TEXT, reply_markup=admin_menu_kb())


@router.callback_query(F.data == "admin:back")
async def cb_back(call: CallbackQuery, state: FSMContext):
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat yo'q", show_alert=True)
        return
    await state.clear()
    await call.message.edit_text(ADMIN_MENU_TEXT, reply_markup=admin_menu_kb())
    await call.answer()


@router.callback_query(F.data == "admin:stats")
async def cb_stats(call: CallbackQuery):
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat yo'q", show_alert=True)
        return
    s = await db.get_stats()
    lines = ["📊 <b>Statistika</b>", ""]
    lines.append(f"👥 Jami foydalanuvchilar: <b>{s['total_users']}</b>")
    lines.append(f"🧪 Jami testlar: <b>{s['total_tests']}</b>")
    lines.append("")
    lines.append("<b>Testlar bo'yicha:</b>")
    for test_id, test in TESTS.items():
        cnt = s["per_test"].get(test_id, 0)
        lines.append(f"  {test['title']}: {cnt}")
    lines.append("")
    lines.append(f"📅 Bugun: <b>{s['today_tests']}</b>")
    lines.append(f"📆 Oxirgi 7 kun: <b>{s['last_7d_tests']}</b>")
    await call.message.edit_text("\n".join(lines), reply_markup=admin_menu_kb())
    await call.answer()


@router.callback_query(F.data == "admin:users")
async def cb_users(call: CallbackQuery):
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat yo'q", show_alert=True)
        return
    s = await db.get_stats()
    recent = await db.get_recent_users(10)
    lines = [f"👥 <b>Foydalanuvchilar</b> (jami: {s['total_users']})", ""]
    if not recent:
        lines.append("Hozircha foydalanuvchilar yo'q.")
    else:
        lines.append("<b>Oxirgi 10 ta:</b>")
        for i, (uid, uname, fname, joined) in enumerate(recent, 1):
            name = fname or "—"
            handle = f"@{uname}" if uname else "—"
            lines.append(f"{i}. {name} ({handle}) — {joined}")
    await call.message.edit_text("\n".join(lines), reply_markup=admin_menu_kb())
    await call.answer()


@router.callback_query(F.data == "admin:broadcast")
async def cb_broadcast(call: CallbackQuery, state: FSMContext):
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat yo'q", show_alert=True)
        return
    await state.set_state(AdminStates.waiting_broadcast)
    await call.message.edit_text(
        "📢 <b>Xabar yuborish (broadcast)</b>\n\n"
        "Yubormoqchi bo'lgan xabaringizni shu yerga yuboring "
        "(matn, rasm, video, ovozli xabar va h.k. — barchasi uzatiladi).\n\n"
        "Bekor qilish uchun /cancel.",
        reply_markup=None,
    )
    await call.answer()


@router.message(StateFilter(AdminStates.waiting_broadcast))
async def do_broadcast(message: Message, bot: Bot, state: FSMContext):
    if not is_admin(message.from_user.id):
        await state.clear()
        return
    await state.clear()

    user_ids = await db.get_all_user_ids()
    total = len(user_ids)
    if total == 0:
        await message.answer("Foydalanuvchilar topilmadi.")
        return

    from_chat = message.chat.id
    msg_id = message.message_id
    sent = 0
    failed = 0
    progress = await message.answer("⏳ Yuborilmoqda...")
    for uid in user_ids:
        try:
            await bot.copy_message(
                chat_id=uid,
                from_chat_id=from_chat,
                message_id=msg_id,
            )
            sent += 1
        except Exception:
            # Foydalanuvchi botni bloklagan/chatni o'chirgan bo'lishi mumkin
            failed += 1
    await progress.edit_text(
        f"✅ Xabar yuborildi.\n\n"
        f"Yetkazildi: <b>{sent}</b> / {total}\n"
        f"Xatolik (bloklangan): {failed}"
    )


@router.callback_query(F.data == "admin:info")
async def cb_info(call: CallbackQuery, bot: Bot, started_at: datetime):
    if not is_admin(call.from_user.id):
        await call.answer("Ruxsat yo'q", show_alert=True)
        return
    me = await bot.get_me()
    uptime = str(datetime.now() - started_at).split(".")[0]
    admins = ", ".join(str(a) for a in ADMIN_IDS) or "—"
    lines = ["ℹ️ <b>Bot haqida</b>", ""]
    lines.append(f"Username: @{me.username}")
    lines.append(f"ID: <code>{me.id}</code>")
    lines.append(f"Ism: {me.first_name}")
    lines.append(f"Admin'lar: {admins}")
    lines.append(f"Ish vaqti: {uptime}")
    await call.message.edit_text("\n".join(lines), reply_markup=admin_menu_kb())
    await call.answer()
