import os
from dotenv import load_dotenv


# import environment vars from .env
load_dotenv()


print(os.getenv('BOT_TELEGRAM_TOKEN'))
