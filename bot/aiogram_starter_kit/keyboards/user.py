from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


web_app = WebAppInfo(url="https://iamihnatiev.github.io")

USER_MENU_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Website", web_app=web_app),
            KeyboardButton(text="Button 2"),
        ],
        [
            KeyboardButton(text="Button 3"),
            KeyboardButton(text="Button 4"),
        ],
    ],
    resize_keyboard=True,
)
