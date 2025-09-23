from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from db.part_object import get_names_category

kb_register = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Зарегистрироваться')]])


def kb_menu(is_admin: bool):
    list_btn = [
        [KeyboardButton(text='Меню 📃'), KeyboardButton(text='Написать отзыв 👨‍💻')]
    ]

    if is_admin is True:
        list_btn.append([KeyboardButton(text='Работа с объектом 🛠️')])

    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=list_btn)


kb_remove = ReplyKeyboardRemove()

kb_restart = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Заново 🔁')]])


def kb_list_category():
    kb = [
            [KeyboardButton(text=cat[0])] for cat in get_names_category()
    ]
    kb.append([KeyboardButton(text='Назад в меню')])
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    return markup


def kb_list_product(list_titles):
    kb = [
        [KeyboardButton(text=title[0])] for title in list_titles
    ]
    kb.append([KeyboardButton(text='Назад в категориям')])
    markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    return markup
