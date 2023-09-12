from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot.common import text
from src.bot.keyboards import USER_MENU_KB
from src.bot.states import RegisterStates
from src.db import Database


register_router = Router(name='register')


@register_router.message(F.text == text.REGISTER_CONFIRM, RegisterStates.confirm)
async def register_confirm(message: Message, state: FSMContext, db: Database):
    await state.clear()

    await db.user.new(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    await message.answer(
        text="Congratulations! You have successfully completed the registration process.",
        reply_markup=USER_MENU_KB,
    )
