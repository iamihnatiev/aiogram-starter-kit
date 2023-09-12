from aiogram import Router
from aiogram.types import Message


unrecognized_router = Router(name='unrecognized')


@unrecognized_router.message()
async def unrecognized(message: Message):
    await message.answer(text="I'm sorry, but I couldn't understand your message.")
