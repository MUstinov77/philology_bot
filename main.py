from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
import logging


from handlers import start_messages, test_messages, accent_test
from config import config
from aiogram.fsm.storage.memory import MemoryStorage


routers = (
    start_messages.router,
    test_messages.router,
    accent_test.router
)
BOT_TOKEN = config.bot_token.get_secret_value()
WEBHOOK_HOST = 'https://filology-bot-6.onrender.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )

dp = Dispatcher(bot=bot, storage=MemoryStorage())
dp.include_routers(*routers)


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(url=WEBHOOK_URL)


async def on_shutdown():
    await bot.delete_webhook()


def main():
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host='0.0.0.0', port=10000)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

