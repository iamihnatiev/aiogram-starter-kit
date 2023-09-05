import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from src.config import conf
from src.bot.utils import set_ui_commands
from src.bot.dispatcher import get_dispatcher
from src.bot.dtos import DatabaseDTO
from src.db.database import get_engine


async def start_bot():
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)
    dp = get_dispatcher()

    # Set bot commands in UI
    await set_ui_commands(bot=bot)

    # Run bot
    await dp.start_polling(bot, **DatabaseDTO(
        engine=get_engine(url=conf.db.build_connection_url()),
    ))


if __name__ == '__main__':
    asyncio.run(start_bot())
