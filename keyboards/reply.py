from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_register = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Зарегистрироваться')]])


def kb_menu(is_admin: bool):
    list_btn = [
        [KeyboardButton(text='Меню 📃'), KeyboardButton(text='Написать отзыв 👨‍💻')]
    ]

    if is_admin is True:
        list_btn.append([KeyboardButton(text='Работа с объектом 🛠️')])

    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=list_btn)
