from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

web_app = WebAppInfo(url='https://iamihnatiev.github.io')

USER_MENU_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Button 1"),
            KeyboardButton(text="Button 2"),
        ],
        [
            KeyboardButton(text="Button 3"),
            KeyboardButton(text="Website", web_app=web_app),
        ]
    ],
    resize_keyboard=True,
)
