from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.bot.filters import AdminFilter


admin_router = Router(name='admin')
admin_router.message.filter(AdminFilter())


@admin_router.message(Command('admin'))
async def admin_command(message: Message):
    await message.answer(text="You have access to admin functionality.")
