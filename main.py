from os import getenv
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from fastapi import FastAPI


# import environment vars from .env
load_dotenv()

BOT_TELEGRAM_TOKEN = getenv('BOT_TELEGRAM_TOKEN')
NGROK_URL = getenv('NGROK_URL')

# FastApi app
app = FastAPI()
WEBHOOK_PATH = f'/webhook/{BOT_TELEGRAM_TOKEN}'
WEBHOOK_URL = f'{NGROK_URL}/{WEBHOOK_PATH}/'


@app.on_event('startup')
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL,
        )