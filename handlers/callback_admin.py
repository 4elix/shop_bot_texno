from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from db.part_user import get_status_admin
from keyboards.inline import kb_work_object, option_object
from keyboards.reply import kb_remove, kb_restart, kb_menu
from db.part_admin import create_category, update_category, create_product, update_product
from utils import CUCategoryState, DeleteCategoryState, CUProductState, DeleteProductState

router_callback_admin = Router()


@router_callback_admin.callback_query(F.data == 'work_categories')
async def react_btn_work_categories(callback: CallbackQuery):
    await callback.message.answer('Хорошо, с данные объектом можно', reply_markup=kb_remove)
    await callback.message.answer('Выполнить данные операции', reply_markup=kb_work_object('categories', 'категорию'))


@router_callback_admin.callback_query(F.data == 'work_products')
async def react_btn_work_products(callback: CallbackQuery):
    await callback.message.answer('Хорошо, с данные объектом можно', reply_markup=kb_remove)
    await callback.message.answer('Выполнить данные операции', reply_markup=kb_work_object('products', 'продукт'))


@router_callback_admin.callback_query(F.data.startswith('create_'))
async def react_btn_create(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(CUCategoryState.name)
        await callback.message.answer('Введите название категории', reply_markup=kb_restart)
    elif obj == 'products':
        await state.set_state(CUProductState.title)
        await callback.message.answer('Введите название товара', reply_markup=kb_restart)


@router_callback_admin.callback_query(F.data.startswith('update_'))
async def react_btn_update(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(CUCategoryState.category_id)
        await callback.message.answer('Введите Id для изменения объекта', reply_markup=kb_restart)
    elif obj == 'products':
        await state.set_state(CUProductState.product_id)
        await callback.message.answer('Введите Id для изменения объекта', reply_markup=kb_restart)


@router_callback_admin.callback_query(F.data.startswith('delete_'))
async def react_btn_delete(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(DeleteCategoryState.category_id)
        await callback.message.answer('Введите Id для удаления объекта', reply_markup=kb_restart)
    elif obj == 'products':
        await state.set_state(DeleteProductState.product_id)
        await callback.message.answer('Введите Id для удаления объекта', reply_markup=kb_restart)


@router_callback_admin.callback_query(F.data == 'category_save')
async def react_btn_save_category(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category_id = data.get('category_id', None)
    category_name = data.get('name')
    await state.clear()

    if category_id is None:
        status = create_category(category_name)
        if status == 200:
            text = 'Категория успешно создана !!!'
        else:
            text = 'Произошла ошибка !!!'

        await callback.message.answer(text, reply_markup=kb_work_object('categories', 'категорию'))
    else:
        status = update_category(category_id, category_name)
        if status == 200:
            text = 'Категория успешно изменена !!!'
        else:
            text = 'Произошла ошибка !!!'

        await callback.message.answer(text, reply_markup=kb_work_object('categories', 'категорию'))


@router_callback_admin.callback_query(F.data == 'category_cancel')
async def react_btn_category_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = 'Хорошо, выберете операцию для объекта'
    await callback.message.answer(text, reply_markup=kb_work_object('categories', 'категорию'))


@router_callback_admin.callback_query(F.data == 'product_save')
async def react_btn_save_product(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    product_id = data.get('product_id', None)
    title, price = data.get('title'), data.get('price')
    quantity, description = data.get('quantity'), data.get('description')
    image, category_id = data.get('image'), data.get('category_id')

    if product_id is None:
        status = create_product(title, price, quantity, description, image, category_id)
        if status == 200:
            text = 'Продукт успешно создан !!!'
        else:
            text = 'Произошла ошибка !!!'

        await callback.message.answer(text, reply_markup=kb_work_object('products', 'продукт'))
    else:
        status = update_product(product_id, title, price, quantity, description, image, category_id)
        if status == 200:
            text = 'Продукт успешно изменен !!!'
        else:
            text = 'Произошла ошибка !!!'

        await callback.message.answer(text, reply_markup=kb_work_object('products', 'продукт'))


@router_callback_admin.callback_query(F.data == 'product_cancel')
async def react_btn_product_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = 'Хорошо, выберете операцию для объекта'
    await callback.message.answer(text, reply_markup=kb_work_object('products', 'продукт'))


@router_callback_admin.callback_query(F.data == 'back_to_menu')
async def react_btn_back_to_menu(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    is_admin = get_status_admin(chat_id)[0]
    await callback.message.answer('Хорошо, вот меню', reply_markup=kb_menu(is_admin))


@router_callback_admin.callback_query(F.data == 'back_to_option')
async def react_btn_back_to_option(callback: CallbackQuery):
    await callback.message.answer('Выберите с каким объектом будете работать', reply_markup=option_object)
