from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

option_object = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Категории', callback_data='work_categories'),
        InlineKeyboardButton(text='Продукты', callback_data='work_products')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='back_to_menu')
    ]
])


def kb_work_object(obj: str, name: str):
    objects = [
        (f'create_{obj}', f'Создать {name}'),
        (f'update_{obj}', f'Изменить {name}'),
        (f'delete_{obj}', f'Удалить {name}')
    ]

    list_btn = []
    for work, name in objects:
        list_btn.append([InlineKeyboardButton(text=name, callback_data=work)])

    list_btn.append([InlineKeyboardButton(text='Назад', callback_data='back_to_option')])
    return InlineKeyboardMarkup(inline_keyboard=list_btn)


kb_category_save_or_cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подтверждаю', callback_data='category_save'),
        InlineKeyboardButton(text='Отменить', callback_data='category_cancel')
    ]
])

kb_product_save_or_cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подтверждаю', callback_data='product_save'),
        InlineKeyboardButton(text='Отменить', callback_data='product_cancel')
    ]
])


def kb_back_menu_or_product(cat_name: str):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад в меню', callback_data='back_menu'),
            InlineKeyboardButton(text='Назад в продукты', callback_data=f'back_to_{cat_name}')
        ]
    ])
    return markup
