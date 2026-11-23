"""Psixologiya testlari Telegram boti — ishga tushiruvchi skript."""

import asyncio
import datetime
import logging
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

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


def _start_health_server() -> None:
    """PaaS (Railway, Render va h.k.) uchun $PORT'da oddiy health endpoint.

    Railway health check uchun HTTP port ochishni kutlaydi. Polling bot
    o'zi port ochmaydi, shu sababli $PORT bo'lsa shu yerda kichik server
    ishga tushadi va "200 ok" qaytaradi. Lokalda $PORT bo'lmasa — hech
    narsa qilmaydi (bot'ga ta'sir yo'q).
    """
    port = os.getenv("PORT")
    if not port:
        return

    class _Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")

        def log_message(self, *args):
            pass

    try:
        server = ThreadingHTTPServer(("0.0.0.0", int(port)), _Handler)
        logging.info("Health server: 0.0.0.0:%s", port)
        server.serve_forever()
    except Exception as exc:
        logging.warning("Health server ishlamadi: %s", exc)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    # aiogram'ning update log'i juda ko'p bo'ladi, shuning uchun pasaytiramiz
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)

    # Ma'lumotlar bazasini ishga tushiramiz
    await db.init_db()

    # PaaS health check uchun kichik server (fon ipida)
    threading.Thread(target=_start_health_server, daemon=True).start()

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
