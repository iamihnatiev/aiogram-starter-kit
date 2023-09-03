import asyncio

from aiogram import Bot
from aiogram.enums import ParseMode

from src.config import conf
from src.bot.dispatcher import get_dispatcher


async def start_bot():
    bot = Bot(token=conf.bot.token, parse_mode=ParseMode.HTML)
    dp = get_dispatcher()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
