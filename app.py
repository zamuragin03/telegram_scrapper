from Commands import check_messages
import logging
from Config import scheduler, bot, dp, router
from pathlib import Path

from aiogram import Dispatcher
from aiogram.types import BotCommand
import asyncio
import logging
from pathlib import Path

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

async def on_startup(dispatcher: Dispatcher):
    scheduler.start() 
    scheduler.add_job(check_messages, 'interval', minutes=1,
                      args=(dp,) )
    

async def on_shutdown(dispatcher: Dispatcher):
    scheduler.shutdown(wait=False)
    logging.info("Scheduler stopped.")

async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    logging.basicConfig(
        filename=Path(__file__).parent.joinpath('DB_volume').joinpath("debug.log"),
        filemode="w",
        level=logging.DEBUG,
        encoding='UTF-8',
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    
    # Include your routers before starting polling
    dp.include_router(router)

    # Run the bot
    asyncio.run(main())