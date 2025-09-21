from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.reply import kb_remove, kb_restart
from keyboards.inline import kb_work_object, kb_category_save_or_cancel
from db.part_admin import create_category, update_category, delete_category
from utils import CUCategoryState, DeleteCategoryState, CUProductState, DeleteProductState

router_callback_admin = Router()


@router_callback_admin.callback_query(F.data == 'work_categories')
async def react_btn_work_categories(callback: CallbackQuery):
    await callback.message.answer('Хорошо, с данные объектом можно', reply_markup=kb_remove)
    await callback.message.answer('Выполнить данные операции', reply_markup=kb_work_object('categories', 'Категорию'))


@router_callback_admin.callback_query(F.data == 'work_products')
async def react_btn_work_products(callback: CallbackQuery):
    await callback.message.answer('Хорошо, с данные объектом можно', reply_markup=kb_remove)
    await callback.message.answer('Выполнить данные операции', reply_markup=kb_work_object('products', 'Продукт'))


@router_callback_admin.callback_query(F.data.startswith('create_'))
async def react_btn_create(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(CUCategoryState.name)
        await callback.answer('Введите название', kb_restart)
    elif obj == 'products':
        await state.set_state(CUProductState.title)
        await callback.answer('Введите название', kb_restart)


@router_callback_admin.callback_query(F.data.startswith('update_'))
async def react_btn_update(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(CUCategoryState.category_id)
        await callback.answer('Введите Id для изменения объекта', kb_restart)
    elif obj == 'products':
        await state.set_state(CUProductState.product_id)
        await callback.answer('Введите Id для изменения объекта', kb_restart)


@router_callback_admin.callback_query(F.data.startswith('delete_'))
async def react_btn_delete(callback: CallbackQuery, state: FSMContext):
    _, obj = callback.data.split('_')

    if obj == 'categories':
        await state.set_state(DeleteCategoryState.category_id)
        await callback.answer('Введите Id для удаления объекта', kb_restart)
    elif obj == 'products':
        await state.set_state(DeleteProductState.product_id)
        await callback.answer('Введите Id для удаления объекта', kb_restart)


@router_callback_admin.callback_query(F.data == 'save_category')
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

        await callback.message.answer(text, reply_markup=kb_work_object('categories', 'Категорию'))
    else:
        status = update_category(category_id, category_name)
        if status == 200:
            text = 'Категория успешно изменена !!!'
        else:
            text = 'Произошла ошибка !!!'

        await callback.message.answer(text, reply_markup=kb_work_object('categories', 'Категорию'))


@router_callback_admin.callback_query(F.data == 'category_cancel')
async def react_btn_category_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = 'Хорошо, выберете операцию для объекта'
    await callback.message.answer(text, reply_markup=kb_work_object('categories', 'Категорию'))
