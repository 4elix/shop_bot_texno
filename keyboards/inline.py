from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

option_object = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Категории', callback_data='work_categories'),
        InlineKeyboardButton(text='Продукты', callback_data='work_products')
    ]
])
