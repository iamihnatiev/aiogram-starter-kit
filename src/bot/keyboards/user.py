from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

USER_MENU_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Button 1"),
            KeyboardButton(text="Button 2"),
        ],
        [
            KeyboardButton(text="Button 3"),
            KeyboardButton(text="Button 4"),
        ]
    ],
    resize_keyboard=True,
)
