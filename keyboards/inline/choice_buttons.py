from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import URL_CPU, URL_GPU, URL_SSD

choice = InlineKeyboardMarkup(row_width=2)

choice_CPU = InlineKeyboardButton(text="CPU's", callback_data="choice:CPU's")
choice.insert(choice_CPU)
choice_GPU = InlineKeyboardButton(text="GPU's", callback_data="choice:GPU's")
choice.insert(choice_GPU)
choice_SSD = InlineKeyboardButton(text="SSD's", callback_data="choice:SSD's")
choice.insert(choice_SSD)

choice_cancel = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(choice_cancel)

cpu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy here", url=URL_CPU)
        ],
    ]
)

gpu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy here", url=URL_GPU)
        ],
    ]
)

ssd_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy here", url=URL_SSD)
        ],
    ]
)
