from aiogram import Router, F
from aiogram.types import Message

from keyboards.inline import option_object


router_txt_admin = Router()


@router_txt_admin.message(F.text == 'Работа с объектом 🛠️')
async def react_btn_work_object(message: Message):
    await message.answer('Выберите с каким объектом будете работать', reply_markup=option_object)

