from aiogram.fsm.state import State, StatesGroup


class RegisterStates(StatesGroup):
    confirm = State()
