from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters.callback_data import CallbackData

class deposit_callback(CallbackData, prefix="deposit_type"):
    deposit_method: str
    deposit_name: str



class deposit_callback(CallbackData, prefix="deposit_type"):
    deposit_method: str
    deposit_name: str


class get_subscription_callback(CallbackData, prefix="get_subscription"):
    duration: int
    price: float


class Keyboard:
    @staticmethod
    def remove():
        return ReplyKeyboardRemove()
    @staticmethod
    def get_actions_kb():
        options = [
            'Посмотреть ключевые слова',
            'Добавить ключевое слово',
            'Удалить ключевое слово'
        ]
        menu_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=options[0])],
                [KeyboardButton(text=options[1])],
                [KeyboardButton(text=options[2])]
            ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        return menu_kb

    def get_menu():
        menu_options = ['💸Баланс💲', '💰Пополнить баланс💳']
        menu_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='🔐Приватный канал🔞')],
                [
                    KeyboardButton(text=menu_options[0]),
                    KeyboardButton(text=menu_options[1]),
                ],
                [KeyboardButton(text='🔗Отзывы✅')],
                [KeyboardButton(text='🆘Помощь🆘')]
            ], resize_keyboard=True, one_time_keyboard=False
        )
        return menu_kb
    
    def get_enter_to_channel_buttons():
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f'🔐Приватный канал🔥', callback_data='enter_private'),
                ]
            ]
        )
        return markup
    
   
    def deposit_kb():
        wd_kb = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text='💰Пополнить баланс💳')],

        ], resize_keyboard=True, one_time_keyboard=False
        )
        return wd_kb
    
    def get_link_to_channel(url):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f'Вступить', callback_data='pizd', url=url),

                ]
            ]
        )
        return markup
    
    def deposit_methods():
        # options = ['⚡️СБП/Карты РФ', 'Aaio']
        options = ['⚡️СБП/Карты РФ',]
        my_options = []
        for option in options:
            my_options.append(
                KeyboardButton(text=str(option)),
            )
        kb_list = [my_options]
        kb_list.append([KeyboardButton(text='◀️Назад◀️')])
        sum_kb = ReplyKeyboardMarkup(
            keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True
        )
        return sum_kb
    
    def proceed_payment(amount, url):
        options = [
            [
                InlineKeyboardButton(
                    text=f'Оплатить({amount}₽)', url=url)
            ],
            [
                InlineKeyboardButton(
                    text=f'Отменить', callback_data='back_to_menu')
            ]
        ]

        payment = InlineKeyboardMarkup(inline_keyboard=options)
        return payment

    def get_link_to_user(button_url):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f'Диалог', url=button_url),
                ],
            ]
        )
        return markup
