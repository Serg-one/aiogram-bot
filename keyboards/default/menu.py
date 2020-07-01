from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CPU's")
        ],
        [
            KeyboardButton(text="GPU's"),
            KeyboardButton(text="SSD's")
        ],
    ],
    resize_keyboard=True
)
