from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

option_object = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Категории', callback_data='work_categories'),
        InlineKeyboardButton(text='Продукты', callback_data='work_products')
    ]
])


def kb_work_object(obj, name):
    list_objects = [
        (f'create_{obj}', f'Создать {name}'),
        (f'update_{obj}', f'Изменить {name}'),
        (f'delete_{obj}', f'Удалить {name}')
    ]

    list_btn = []
    for work, name in list_objects:
        list_btn.append([InlineKeyboardButton(text=name, callback_data=work)])

    return InlineKeyboardMarkup(inline_keyboard=list_btn)


kb_category_save_or_cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подтверждаю', callback_data='category_save'),
        InlineKeyboardButton(text='Отменить', callback_data='category_cancel')
    ]
])

