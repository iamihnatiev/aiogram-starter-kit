from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.db import Database
from src.bot.services import UserService
from src.bot.dtos import UserDTO

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: Message, db: Database):
    user_service = UserService(db=db)

    user: UserDTO = await user_service.get_user(user_id=message.from_user.id)

    await message.answer(text=f"Hello, {html.bold(user['first_name'])}!")
