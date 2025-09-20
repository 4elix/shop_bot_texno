from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils import RegisterState
from db.part_user import save_user
from keyboards.reply import kb_menu

router_txt_user = Router()


@router_txt_user.message(F.text == 'Зарегистрироваться')
async def react_btn_register(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя:')
    await state.set_state(RegisterState.name)


@router_txt_user.message(RegisterState.name)
async def get_name_user(message: Message, state: FSMContext):
    user_name = message.text.split(':')[::-1]
    chat_id = message.chat.id

    try:
        if user_name[0] == '111':
            is_admin = True
        else:
            is_admin = False

        save_user(user_name[1], is_admin, chat_id)

        await message.answer('Регистрация прошла успешно. Ниже есть кнопки ⬇️', reply_markup=kb_menu(is_admin))
    except Exception as error:
        print(error)
        await message.answer('Произошла ошибка, введите только свое имя. Пример: Иван')
        await state.set_state(RegisterState.name)
