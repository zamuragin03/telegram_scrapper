import configparser
from pathlib import Path
import sys

config = configparser.ConfigParser()
PATH = Path(__file__).resolve().parent
config.read(str(PATH) + '/config.ini')

BOT_TOKEN = config["Telegram"]["bot_token"]
PATH_TO_DB = PATH.parent.joinpath('DB_volume').joinpath('data.db')

API_ID = config['Telethon']['api_id']
API_HASH = str(config['Telethon']['api_hash'])
PHONE = config['Telethon']['phone']

SERVICE_CHAT_ID = -1002217943042



