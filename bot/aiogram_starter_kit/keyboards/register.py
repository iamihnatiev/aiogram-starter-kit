from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from aiogram_starter_kit.common import text


REGISTER_CONFIRM_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=text.REGISTER_CONFIRM),
        ]
    ],
    resize_keyboard=True,
)
