from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Choose category from menu above:", reply_markup=menu)


@dp.message_handler(Text(equals=["CPU's", "GPU's", "SSD's"]))
async def get_category(message: Message):
    await message.answer(f"You choose {message.text}. Thanks", reply_markup=ReplyKeyboardRemove())
