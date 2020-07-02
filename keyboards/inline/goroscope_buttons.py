from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import zodiac_callback

goroscope = InlineKeyboardMarkup()

key_oven = InlineKeyboardButton(text="♈ Овен", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_oven)
key_telec = InlineKeyboardButton(text="♉ Телец", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_telec)
key_bliznecy = InlineKeyboardButton(text="♊ Близнецы", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_bliznecy)
key_rak = InlineKeyboardButton(text="♋ Рак", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_rak)
key_lev = InlineKeyboardButton(text="♌ Лев", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_lev)
key_deva = InlineKeyboardButton(text="♍ Дева", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_deva)
key_vesy = InlineKeyboardButton(text="♎ Весы", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_vesy)
key_scorpion = InlineKeyboardButton(text="♏ Скорпион", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_scorpion)
key_strelec = InlineKeyboardButton(text="♐ Стрелец", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_strelec)
key_kozerog = InlineKeyboardButton(text="♑ Козерог", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_kozerog)
key_vodoley = InlineKeyboardButton(text="♒ Водолей", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_vodoley)
key_ryby = InlineKeyboardButton(text="♓ Рыбы", callback_data=zodiac_callback.new("zodiac"))
goroscope.insert(key_ryby)

key_cancel = InlineKeyboardButton(text="↩️ Back", callback_data=zodiac_callback.new("Back"))
goroscope.insert(key_cancel)
