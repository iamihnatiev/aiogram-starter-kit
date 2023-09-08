from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from src.bot.common import text

REGISTER_CONFIRM_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=text.REGISTER_CONFIRM),
        ]
    ],
    resize_keyboard=True,
)
