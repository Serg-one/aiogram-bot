import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
URL_CPU = os.getenv("URL_CPU")
URL_GPU = os.getenv("URL_GPU")
URL_SSD = os.getenv("URL_SSD")
admins = [
    os.getenv("ADMIN_IP"),
    ]

ip = os.getenv("IP")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
