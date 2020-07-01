import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import choice_callback
from keyboards.inline.choice_buttons import choice, cpu_keyboard, gpu_keyboard, ssd_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="Choose a category. \nOr press cancel", reply_markup=choice)


@dp.callback_query_handler(choice_callback.filter(item_name="CPU"))
async def choose_cpu(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer("Your choose CPU's. Thanks", reply_markup=cpu_keyboard)


@dp.callback_query_handler(choice_callback.filter(item_name="GPU"))
async def choose_gpu(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer("Your choose GPU's. Thanks", reply_markup=gpu_keyboard)


@dp.callback_query_handler(choice_callback.filter(item_name="SSD"))
async def choose_ssd(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    await call.message.answer("Your choose SSD's. Thanks", reply_markup=ssd_keyboard)


@dp.callback_query_handler(text="Cancel")
async def choose_cancel(call: CallbackQuery):
    await call.answer("You canceled purchase!", show_alert=True)
    await call.message.edit_reply_markup()
