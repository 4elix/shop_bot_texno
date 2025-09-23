from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils import ShowProduct
from db.part_user import get_status_admin
from keyboards.reply import kb_menu, kb_list_product
from db.part_object import get_product_title_for_category

router_callback_user = Router()


@router_callback_user.callback_query(F.data == 'back_menu')
async def react_btn_back_menu(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    is_admin = get_status_admin(chat_id)[0]
    await callback.message.answer('Хорошо, вот меню', reply_markup=kb_menu(is_admin))


@router_callback_user.callback_query(F.data.startswith('back_to_'))
async def react_btn_back_to_category(callback: CallbackQuery, state: FSMContext):
    _, _, cat_name = callback.data.split('_')
    text = 'Хорошо, вот список продуктов данной категории'
    list_title_products = get_product_title_for_category(cat_name)
    await callback.message.answer(text, reply_markup=kb_list_product(list_title_products))
    await state.set_state(ShowProduct.cat_name)
    await state.update_data(cat_name=cat_name)
