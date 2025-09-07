import logging
import os
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
from handlers import start_handler, client_handler

# loglar
logging.basicConfig(level=logging.INFO)

# .env dan token va admin_id olish
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))  # faqat bitta admin

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# handlerlar
dp.register_message_handler(start_handler, commands=["start"])
dp.register_message_handler(lambda msg: client_handler(msg, bot, ADMIN_ID))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
