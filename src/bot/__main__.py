import logging
import asyncio

from redis.asyncio.client import Redis

from aiogram import Bot
from aiogram.enums import ParseMode

from src.config import conf
from src.bot.utils import set_ui_commands
from src.bot.dispatcher import get_dispatcher, get_redis_storage
from src.bot.dtos import DatabaseDTO
from src.db.database import get_engine


async def start_bot():
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)

    storage = get_redis_storage(redis=Redis(
        password=conf.redis.password,
        host=conf.redis.host,
        port=conf.redis.port,
        db=conf.redis.db,
    ))

    dp = get_dispatcher(storage=storage)

    # Set bot commands in UI
    await set_ui_commands(bot=bot)

    # Run bot
    await dp.start_polling(bot, **DatabaseDTO(
        engine=get_engine(url=conf.db.build_connection_url()),
    ))


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging_level)
    asyncio.run(start_bot())
