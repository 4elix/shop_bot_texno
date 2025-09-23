from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from support import text_info_product
from utils import RegisterState, ShowProduct
from db.part_user import save_user, get_status_admin
from keyboards.inline import kb_back_menu_or_product
from keyboards.reply import kb_menu, kb_list_category, kb_list_product, kb_remove
from db.part_object import get_names_category, get_product_title_for_category, get_info_product

router_txt_user = Router()


@router_txt_user.message(F.text == 'Зарегистрироваться')
async def react_btn_register(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя:')
    await state.set_state(RegisterState.name)


@router_txt_user.message(RegisterState.name)
async def get_name_user(message: Message, state: FSMContext):
    user_name = message.text.split(':')[::-1]
    chat_id = message.chat.id
    await state.clear()

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


@router_txt_user.message(F.text == 'Меню 📃')
async def react_btn_show_menu(message: Message):
    await message.answer('Нажмите на кнопку для выбора категории', reply_markup=kb_list_category())


@router_txt_user.message(F.text.in_([name[0] for name in get_names_category()]))
async def react_btn_show_category(message: Message, state: FSMContext):
    text = 'Хорошо, вот список продуктов данной категории'
    list_title_products = get_product_title_for_category(message.text)
    await message.answer(text, reply_markup=kb_list_product(list_title_products))
    await state.set_state(ShowProduct.cat_name)
    await state.update_data(cat_name=message.text)

    await state.set_state(ShowProduct.title)


@router_txt_user.message(ShowProduct.title)
async def get_product_title(message: Message, state: FSMContext):
    title = message.text
    data = await state.get_data()

    if title == 'Назад в категориям':
        await state.clear()
        await message.answer('Хорошо, выберете другую категорию', reply_markup=kb_list_category())
        return

    status = get_info_product(title)
    if status == 404:
        cat_name = data['cat_name']
        text = 'Произошла ошибка, нажмите на кнопку ниже для выбора товара ⬇️'
        await message.answer(text, reply_markup=kb_list_product(cat_name))
    else:
        _, title, price, quantity, description, image, _ = status
        cat_name = data['cat_name']
        await state.clear()
        text = text_info_product(title, price, quantity, description, cat_name)
        await message.answer_photo(photo=FSInputFile(image), caption=text, reply_markup=kb_remove)
        await message.answer('Можете посмотреть ещё новости или в меню', reply_markup=kb_back_menu_or_product(cat_name))


@router_txt_user.message(F.text == 'Назад в меню')
async def react_btnr_back_to_menu(message: Message, state: FSMContext):
    await state.clear()
    chat_id = message.chat.id
    is_admin = get_status_admin(chat_id)[0]
    await message.answer('Хорошо, вот меню', reply_markup=kb_menu(is_admin))
