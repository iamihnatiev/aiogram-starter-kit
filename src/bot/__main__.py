import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from aiogram import Bot
from aiogram.enums import ParseMode

from src.config import conf
from src.bot.dispatcher import get_dispatcher
from src.bot.structures import TransferData


async def start_bot():
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)
    dp = get_dispatcher()

    await dp.start_polling(bot, **TransferData(
        engine=create_async_engine(url=conf.db.build_connection_url()),
    ))


if __name__ == '__main__':
    asyncio.run(start_bot())
