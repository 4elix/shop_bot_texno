def text_id_name_category(obj: list) -> str:
    text = ''
    for cat_id, cat_name in obj:
        text += f'Id: {cat_id} -- Категория: {cat_name}'

    return text


def text_product_state(obj: dict) -> str:
    product_id = obj.get('product_id')
    title = obj.get('title')
    price = obj.get('price')
    quantity = obj.get('quantity')
    description = obj.get('description')
    image = obj.get('image')
    category_id = obj.get('category_id')

    text = f'''
Id продукта: {product_id}
Название: {title}
Стоимость: {price}
Кол-во на складе: {quantity}
Описание: {description}
Путь до картинке: {image}
Id категории: {category_id}
'''
    return text
