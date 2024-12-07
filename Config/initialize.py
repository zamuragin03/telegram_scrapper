from DBRepository.DBRepository import DBRepository
from .const import BOT_TOKEN, PATH_TO_DB, PHONE, API_HASH,API_ID
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from telethon.sync import TelegramClient


scheduler = AsyncIOScheduler()
bot = Bot(BOT_TOKEN,)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
Repository = DBRepository(PATH_TO_DB)

client = TelegramClient(PHONE,API_ID, API_HASH)





