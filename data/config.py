import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

IP = os.getenv("IP")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")

aiogram_redis = {
    'host': IP,
}

redis = {
    'address': (IP, 6379),
    'encoding': 'utf8'
}

URL_CPU = os.getenv("URL_CPU")
URL_GPU = os.getenv("URL_GPU")
URL_SSD = os.getenv("URL_SSD")
