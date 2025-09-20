from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from db.part_user import check_register_user
from keyboards.reply import kb_register


router_cmd = Router()


@router_cmd.message(Command('start'))
async def react_cmd_start(message: Message, state: FSMContext):
    status_register = check_register_user(message.chat.id)
    await state.clear()

    if status_register == 404:
        text = 'Здравствуйте, вам нужно зарегистрироваться. Нажмите кнопку ниже ⬇️⬇️⬇️'
        await message.answer(text, reply_markup=kb_register)
    else:
        text = '''
Здравствуйте, данные бот показывает нашу продукцию. 

Нажмите на предлагаемые кнопки ниже ⬇️⬇️⬇️
'''
        await message.answer(text)
