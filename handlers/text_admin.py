from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from db.part_admin import delete_category
from keyboards.inline import kb_work_object, kb_category_save_or_cancel, option_object
from utils import CUCategoryState, DeleteCategoryState, CUProductState, DeleteProductState

router_txt_admin = Router()


@router_txt_admin.message(F.text == 'Работа с объектом 🛠️')
async def react_btn_work_object(message: Message):
    await message.answer('Выберите с каким объектом будете работать', reply_markup=option_object)


@router_txt_admin.message(CUCategoryState.category_id)
async def get_category_id(message: Message, state: FSMContext):
    try:
        cat_id = int(message.message.text)
        await state.update_data(category_id=cat_id)
        await state.set_state(CUCategoryState.name)
        await message.answer('Введите название категории')
    except Exception as error:
        print(error)
        await state.set_state(CUCategoryState.category_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')


@router_txt_admin.message(CUCategoryState.name)
async def get_category_name(message: Message, state: FSMContext):
    await state.update_data(name=message.message.text)
    await message.answer('Отлично, подтвердите результат')

    data = await state.get_data()
    cat_id = data.get('category_id', 'Не указанно')
    name = data['name']
    result = f'ID категории: {cat_id}.\nНазвание категории: {name}'
    await message.answer(result, reply_markup=kb_category_save_or_cancel)


@router_txt_admin.message(DeleteCategoryState.category_id)
async def get_category_id_for_delete(message: Message, state: FSMContext):
    try:
        category_id = int(message.text)
        status = delete_category(category_id)
        if status == 200:
            text = 'Категория успешно удалена'
        else:
            text = 'Произошла ошибка при удалении'

        await message.answer(text, reply_markup=kb_work_object('categories', 'Категорию'))
    except Exception as error:
        print(error)
        await state.set_state(DeleteCategoryState.category_id)
        await message.answer('Произошла ошибка, введите Id корректно. Например: 3')
