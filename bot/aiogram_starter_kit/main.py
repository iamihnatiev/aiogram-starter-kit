from aiogram import Bot
from aiogram.enums import ParseMode
from redis.asyncio.client import Redis

from aiogram_starter_kit.configuration import conf
from aiogram_starter_kit.dispatcher import get_dispatcher, get_redis_storage
from aiogram_starter_kit.structures.dtos import DatabaseDTO
from aiogram_starter_kit.utils import set_ui_commands
from db.database import get_engine


async def start_bot() -> None:
    """
    Start the Aiogram bot with configuration settings.

    This function initializes the Aiogram bot, sets up the Redis storage, creates a Dispatcher, and starts
    the bot with the specified settings.
    """
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)

    storage = get_redis_storage(
        redis=Redis(
            host=conf.redis.host,
            port=conf.redis.port,
            db=conf.redis.db,
        )
    )

    dp = get_dispatcher(storage=storage)

    # Set bot commands in UI
    await set_ui_commands(bot=bot)

    # Run bot
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        **DatabaseDTO(
            engine=get_engine(connection_url=conf.db.build_connection_url()),
        ),
    )
