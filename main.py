from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.fsm.strategy import FSMStrategy

import asyncio

from handlers import (
    start_messages,
    test_messages,
    accent_test,
    admin_panel,
)
from config import config
from aiogram.fsm.storage.memory import MemoryStorage
from db import db



routers = (
    start_messages.router,
    test_messages.router,
    accent_test.router,
    admin_panel.router
)


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(),
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML
              )
              )

    dp = Dispatcher(
        storage=MemoryStorage(),
        fsm_strategy=FSMStrategy.USER_IN_CHAT
    )
    dp.include_routers(*routers)
    await bot.delete_webhook(drop_pending_updates=True)
    await db.initialize_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())