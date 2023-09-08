from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

REGISTER_CONFIRM_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Register"),
        ]
    ],
    resize_keyboard=True,
)
