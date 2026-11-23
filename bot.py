"""Psixologiya testlari Telegram boti — ishga tushiruvchi skript."""

import asyncio
import datetime
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers.admin import router as admin_router
from handlers.common import router as common_router
from handlers.testing import router as testing_router
import db


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    # aiogram'ning update log'i juda ko'p bo'ladi, shuning uchun pasaytiramiz
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)

    # Ma'lumotlar bazasini ishga tushiramiz
    await db.init_db()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())
    # Tartib muhim: common -> admin -> testing (testing'dagi catch-all eng oxirda)
    dp.include_router(common_router)
    dp.include_router(admin_router)
    dp.include_router(testing_router)

    # Handler'larga uzatiladigan umumiy ma'lumot (workflow_data)
    dp["started_at"] = datetime.datetime.now()

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Bosh menyu / testlar"),
            BotCommand(command="help", description="Yordam"),
            BotCommand(command="cancel", description="Testni to'xtatish"),
            BotCommand(command="admin", description="Admin panel (admin'larga)"),
        ]
    )

    me = await bot.get_me()
    logging.info("Bot ishga tushdi: @%s (id=%s)", me.username, me.id)
    logging.info("To'xtatish uchun: Ctrl+C")

    try:
        await dp.start_polling(bot)
    finally:
        await db.close_db()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi.")
