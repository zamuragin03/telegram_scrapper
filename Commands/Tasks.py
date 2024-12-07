from Config import client, SERVICE_CHAT_ID
from Config import scheduler, dp, bot
from aiogram import Dispatcher
from random import randint
from Keyboards import Keyboard

from Service import KeywordService, ParseMessagesService

async def get_messages():
    async with client:
        messages = await client.get_messages('by_ot_ka', limit=100)
        return filter(ParseMessagesService.FilterLastMinuteMessages, messages)
        

async def check_messages(dp: Dispatcher):
    messages = await get_messages()
    filtered_message = await KeywordService.FilterMessage(messages)
    for mes in filtered_message:
        await bot.send_message(
            SERVICE_CHAT_ID,
            f'Интересное сообщение от @{mes["entity"].username} {mes["message"].text}\n\n<a href ="https://t.me/by_ot_ka/{mes["message"].id}">Перейти</a>',
            parse_mode='HTML'
            )