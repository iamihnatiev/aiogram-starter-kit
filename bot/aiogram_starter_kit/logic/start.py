from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from aiogram_starter_kit.filters import RegisterFilter
from aiogram_starter_kit.keyboards import REGISTER_CONFIRM_KB, USER_KB
from aiogram_starter_kit.structures.states import RegisterStates


start_router = Router(name="start")


@start_router.message(CommandStart(), RegisterFilter())
async def start_wo_register(message: Message, state: FSMContext) -> None:
    await state.set_state(RegisterStates.confirm)
    await message.answer(text="Welcome to the registration process.", reply_markup=REGISTER_CONFIRM_KB)


@start_router.message(CommandStart())
async def start_w_register(message: Message) -> None:
    await message.answer(
        text=f"Welcome back, {html.bold(message.from_user.first_name)}.",
        reply_markup=USER_KB,
    )
