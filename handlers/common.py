"""Umumiy handler'lar: /start, /help, /cancel va menyu."""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from data.tests import DISCLAIMER
from keyboards import tests_menu_kb
import db

router = Router(name="common")


@router.message(CommandStart())
async def cmd_start(message: Message):
    # Foydalanuvchini bazaga yozib qo'yamiz (yoki yangilaymiz)
    await db.add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
    )
    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "Men — psixologiya testlari botiman. Quyidagi "
        "testlardan birini tanlang va o'zingizni sinab ko'ring.\n\n"
        f"{DISCLAIMER}",
        reply_markup=tests_menu_kb(),
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "ℹ️ Yordam\n\n"
        "/start — bosh menyu va testlar ro'yxati\n"
        "/help — ushbu yordam matni\n"
        "/cancel — testni to'xtatish\n\n"
        "Testni boshlash uchun menyudagi tugmani bosing. "
        "Har bir savolga javobni inline tugma orqali belilang.\n\n"
        f"{DISCLAIMER}"
    )


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Test to'xtatildi. 🛑\nBosh menyu uchun /start",
        reply_markup=tests_menu_kb(),
    )


@router.callback_query(F.data == "help")
async def cb_help(call: CallbackQuery):
    await call.message.answer(
        "ℹ️ Yordam\n\n"
        "/start — bosh menyu\n"
        "/help — yordam\n"
        "/cancel — testni to'xtatish\n\n"
        f"{DISCLAIMER}"
    )
    await call.answer()


@router.callback_query(F.data == "menu")
async def cb_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text(
        "📋 Bosh menyu — testlardan birini tanlang:",
        reply_markup=tests_menu_kb(),
    )
    await call.answer()
