from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import URL_CPU, URL_GPU, URL_SSD
from keyboards.inline.callback_datas import choice_callback

choice = InlineKeyboardMarkup(row_width=2)

choice_CPU = InlineKeyboardButton(text="💻  CPU's", callback_data=choice_callback.new("CPU's"))
choice.insert(choice_CPU)
choice_GPU = InlineKeyboardButton(text="📺  GPU's", callback_data=choice_callback.new("GPU's"))
choice.insert(choice_GPU)
choice_SSD = InlineKeyboardButton(text="💾  SSD's", callback_data=choice_callback.new("SSD's"))
choice.insert(choice_SSD)

choice_cancel = InlineKeyboardButton(text="❌  Cancel", callback_data=choice_callback.new("Cancel"))
choice.insert(choice_cancel)

cpu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💵       Buy here", url=URL_CPU)
        ],
        [
            InlineKeyboardButton(text=u"↩️     Back", callback_data=choice_callback.new("Back"))
        ],
    ]
)

gpu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💵       Buy here", url=URL_GPU)
        ],
        [
            InlineKeyboardButton(text=u"↩️     Back", callback_data=choice_callback.new("Back"))
        ],
    ]
)

ssd_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💵       Buy here", url=URL_SSD)
        ],
        [
            InlineKeyboardButton(text=u"↩️     Back", callback_data=choice_callback.new("Back"))
        ],
    ]
)
