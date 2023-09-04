from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.db import Database

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: Message, db: Database):
    await db.user.find(ident=message.from_user.id)

    await message.answer(text=f"Hello, {html.bold(message.from_user.first_name)}!")
