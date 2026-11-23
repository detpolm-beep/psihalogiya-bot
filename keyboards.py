"""Inline tugmalar (klaviaturalar) yig'uvchi funksiyalar."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.tests import TESTS


def tests_menu_kb() -> InlineKeyboardMarkup:
    """Asosiy menyu — testlar ro'yxati."""
    kb = InlineKeyboardBuilder()
    for test_id, test in TESTS.items():
        kb.button(text=test["title"], callback_data=f"select:{test_id}")
    kb.button(text="ℹ️ Yordam", callback_data="help")
    kb.adjust(1)  # har bir tugma alohida qatorda
    return kb.as_markup()


def question_kb(options: list) -> InlineKeyboardMarkup:
    """Bitta savol uchun javob variantlari tugmalari."""
    kb = InlineKeyboardBuilder()
    for i, option in enumerate(options):
        kb.button(text=option["text"], callback_data=f"ans:{i}")
    kb.button(text="⏹️ To'xtatish", callback_data="cancel")
    kb.adjust(1)
    return kb.as_markup()


def result_kb(test_id: str) -> InlineKeyboardMarkup:
    """Test yakunidagi tugmalar."""
    kb = InlineKeyboardBuilder()
    kb.button(text="🔁 Qayta urinish", callback_data=f"select:{test_id}")
    kb.button(text="📋 Boshqa test", callback_data="menu")
    kb.adjust(1)
    return kb.as_markup()


def admin_menu_kb() -> InlineKeyboardMarkup:
    """Admin panel asosiy menyusi."""
    kb = InlineKeyboardBuilder()
    kb.button(text="📊 Statistika", callback_data="admin:stats")
    kb.button(text="👥 Foydalanuvchilar", callback_data="admin:users")
    kb.button(text="📢 Xabar yuborish", callback_data="admin:broadcast")
    kb.button(text="ℹ️ Bot haqida", callback_data="admin:info")
    kb.adjust(1)
    return kb.as_markup()
