from Config import dp, bot, router
from Keyboards.keyboards import Keyboard
from Service import KeywordService
from aiogram import F
from States import FSMAdmin
from aiogram.fsm.context import FSMContext
from aiogram.filters import *
from aiogram.types import FSInputFile

from aiogram.enums.parse_mode import ParseMode
from aiogram import types
    
ADMINS = [439592830, 225529144]
    
@router.message(Command("admin_menu"))
async def start(message: types.Message, state: FSMContext):
    if message.from_user.id not in ADMINS:
        return
    await message.answer(
        'Выберите действие',
        reply_markup=Keyboard.get_actions_kb()
    )
    await state.set_state(FSMAdmin.choosing_action)

@router.message(
    FSMAdmin.choosing_action,
    F.text.contains('Посмотреть ключевые слова')
)
@router.message(
    FSMAdmin.typing_new_keyword,
    F.text.contains('Посмотреть ключевые слова')
)
async def check_all_keywords(message: types.Message, state: FSMContext):
    keywords = KeywordService.GetAllKeywords()
    await message.answer(
        keywords,
    )
    
@router.message(
    FSMAdmin.choosing_action,
    F.text.contains('Добавить ключевое слово')
)
async def typing_new(message: types.Message, state: FSMContext):
    await message.answer(
        'Введите новое ключевое слово',
    )
    await state.set_state(FSMAdmin.typing_new_keyword)
    
@router.message(
    FSMAdmin.typing_new_keyword,
)
async def add_new(message: types.Message, state: FSMContext):
    if KeywordService.AddNewKeyWord(message.text):
        await message.answer(
        f'Ключевое слово {message.text} успешно добавлено ',
        reply_markup=Keyboard.get_actions_kb()

    )
    else:
        await message.answer(
        f'При добавлении слова произошла ошибка, возможно оно уже добавлено',
    )
    await state.set_state(FSMAdmin.choosing_action)

    
@router.message(
    FSMAdmin.choosing_action,
    F.text.contains('Удалить ключевое слово')
)
async def check_all_keywords(message: types.Message, state: FSMContext):
    keywords = KeywordService.GetAllKeywords()
    message = await message.answer(
        'Введите id ключевого слова, которое хотите удалить',
    )
    await message.reply(keywords)
    await state.set_state(FSMAdmin.selecting_keyword_to_remove)
    
    
    
@router.message(
    FSMAdmin.selecting_keyword_to_remove,
)
async def check_all_keywords(message: types.Message, state: FSMContext):
    try:
        int(message.text)
    except Exception as e:
        await message.answer(
        'Введите корректный id ключевого слова',
    )
    if KeywordService.RemoveKeywordById(message.text):
        await message.answer(
        f'Ключевое слово {message.text} удалено успешно',
        reply_markup=Keyboard.get_actions_kb()
        
    )
    else:
        await message.answer(
        f'Ключевое слово не удалено, так как не найдено.',
        reply_markup=Keyboard.get_actions_kb()
    )
        
    await state.set_state(FSMAdmin.choosing_action)
    
    
    
