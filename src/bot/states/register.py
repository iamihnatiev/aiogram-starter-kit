from aiogram.fsm.state import StatesGroup, State


class RegisterStates(StatesGroup):
    confirm = State()
