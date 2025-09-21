from aiogram.fsm.state import StatesGroup, State


class RegisterState(StatesGroup):
    name = State()


class CUCategoryState(StatesGroup):
    category_id = State()
    name = State()


class DeleteCategoryState(StatesGroup):
    category_id = State()


class CUProductState(StatesGroup):
    product_id = State()
    title = State()
    price = State()
    quantity = State()
    description = State()
    category_id = State()


class DeleteProductState(StatesGroup):
    product_id = State()