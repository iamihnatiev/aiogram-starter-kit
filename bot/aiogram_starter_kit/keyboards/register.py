from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from aiogram_starter_kit.utils import constants


REGISTER_CONFIRM_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=constants.REGISTER_CONFIRM),
        ]
    ],
    resize_keyboard=True,
)
