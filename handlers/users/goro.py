import logging
import random

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import zodiac_callback
from keyboards.inline.goroscope_buttons import goroscope
from loader import dp, bot

first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


# def create_goroscope():
#     msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' \
#           + random.choice(third)
#     return msg


@dp.message_handler(Command('goro'))
async def start_goroscope(message: Message):
    await message.answer("Выберите знак для которого хотите получить гороскоп: \n", reply_markup=goroscope)


@dp.callback_query_handler(zodiac_callback.filter(item_name="zodiac"))
async def choose_cpu(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + \
          ' ' + random.choice(third)
    await call.message.answer(msg, reply_markup=None)


@dp.callback_query_handler(zodiac_callback.filter(item_name="Back"))
async def choose_back(call: CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id, text="Введите другую команду", reply_markup=None)
