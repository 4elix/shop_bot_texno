import os
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from db.part_object import get_all_categories
from db.part_admin import delete_category, delete_product
from support import text_id_name_category, text_product_state
from keyboards.inline import kb_work_object, kb_category_save_or_cancel, option_object, kb_product_save_or_cancel
from utils import CUCategoryState, DeleteCategoryState, CUProductState, DeleteProductState

router_txt_admin = Router()


@router_txt_admin.message(F.text == 'Работа с объектом 🛠️')
async def react_btn_work_object(message: Message):
    await message.answer('Выберите с каким объектом будете работать', reply_markup=option_object)


@router_txt_admin.message(CUCategoryState.category_id)
async def get_category_id(message: Message, state: FSMContext):
    try:
        await state.update_data(category_id=int(message.text))
        await state.set_state(CUCategoryState.name)
        await message.answer('Введите название категории')
    except Exception as error:
        print(error)
        await state.set_state(CUCategoryState.category_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')


@router_txt_admin.message(CUCategoryState.name)
async def get_category_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Отлично, подтвердите результат')

    data = await state.get_data()
    cat_id = data.get('category_id', 'Не указанно')
    name = data['name']
    result = f'ID категории: {cat_id}.\nНазвание категории: {name}'
    await message.answer(result, reply_markup=kb_category_save_or_cancel)


@router_txt_admin.message(DeleteCategoryState.category_id)
async def get_category_id_for_delete(message: Message, state: FSMContext):
    await state.clear()

    try:
        status = delete_category(int(message.text))
        if status == 200:
            text = 'Категория успешно удалена'
        else:
            text = 'Произошла ошибка при удалении'

        await message.answer(text, reply_markup=kb_work_object('categories', 'категорию'))
    except Exception as error:
        print(error)
        await state.set_state(DeleteCategoryState.category_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')


@router_txt_admin.message(CUProductState.product_id)
async def get_product_id(message: Message, state: FSMContext):
    try:
        await state.update_data(product_id=int(message.text))
        await message.answer('Введите название продукту')
    except Exception as error:
        print(error)
        await state.set_state(CUProductState.product_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')


@router_txt_admin.message(CUProductState.title)
async def get_product_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(CUProductState.price)
    await message.answer('Введите стоимость товара')


@router_txt_admin.message(CUProductState.price)
async def get_product_price(message: Message, state: FSMContext):
    try:
        await state.update_data(price=float(message.text))
        await state.set_state(CUProductState.quantity)
        await message.answer('Введите кол-во товаров на складе')
    except Exception as error:
        print(error)
        await state.set_state(CUProductState.price)
        await message.answer('Произошла ошибка, введите корректно стоимость. Например: 200 или 75.22')


@router_txt_admin.message(CUProductState.quantity)
async def get_product_quantity(message: Message, state: FSMContext):
    try:
        await state.update_data(quantity=int(message.text))
        await state.set_state(CUProductState.description)
        await message.answer('Введите описание товара')
    except Exception as error:
        print(error)
        await state.set_state(CUProductState.quantity)
        await message.answer('Произошла ошибка, введите корректно кол-во товара. Например: 88')


@router_txt_admin.message(CUProductState.description)
async def get_product_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(CUProductState.image)
    await message.answer('Отправьте фотографию товара')


@router_txt_admin.message(CUProductState.image)
async def get_product_image(message: Message, state: FSMContext, bot: Bot):
    try:
        folder = 'media/images/'
        if not os.path.exists(folder):
            os.makedirs(folder)

        photo = message.photo[-1]
        photo_file_id = photo.file_id
        file = await bot.get_file(photo_file_id)
        file_path = os.path.join(folder, f'{photo_file_id}.jpg')
        await bot.download_file(file.file_path, destination=file_path)
        await state.update_data(image=f'{folder}/{photo_file_id}.jpg')

        await message.answer('Введите Id категории, вот список категорий:')
        text_categories = text_id_name_category(get_all_categories())
        await message.answer(text_categories)
        await state.set_state(CUProductState.category_id)
    except Exception as error:
        print(error)
        await state.set_state(CUProductState.image)
        await message.answer('Произошла ошибка, отправьте фотограф повторно')


@router_txt_admin.message(CUProductState.category_id)
async def get_category_id_for_product(message: Message, state: FSMContext):
    try:
        await state.update_data(category_id=int(message.text))
        data = await state.get_data()
        text = text_product_state(data)
        await message.answer(text, reply_markup=kb_product_save_or_cancel)
    except Exception as error:
        print(error)
        await state.set_state(CUProductState.category_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')


@router_txt_admin.message(DeleteProductState.product_id)
async def get_product_id_for_delete(message: Message, state: FSMContext):
    await state.clear()

    try:
        status = delete_product(int(message.text))
        if status == 200:
            text = 'Продукт успешно удален'
        else:
            text = 'Произошла ошибка при удалении'

        await message.answer(text, reply_markup=kb_work_object('products', 'продукт'))
    except Exception as error:
        print(error)
        await state.set_state(DeleteProductState.product_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')