from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=f"Hello, {html.bold(message.from_user.first_name)}!")
