try:
    from .db_config import connect_db
except:
    from db_config import connect_db


def create_category(name: str) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('INSERT INTO categories (name) VALUES (%s)', (name, ))
        connect.commit()
        return 200
    except Exception as error:
        print(error)
        return 404


def update_category(id_category: int, name: str) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('UPDATE category SET category_name = %s WHERE category_id = %s', (name, id_category))
        connect.commit()

        return 200
    except Exception as error:
        print(error)
        return 404


def delete_category(id_category: int) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('DELETE FROM categories WHERE category_id = %s', (id_category, ))
        connect.commit()

        return 200
    except Exception as error:
        print(error)
        return 404


def create_product(title: str, price: float, quantity: int,
                   description: str, image: str, category_id: int) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('''
        INSERT INTO products(
            title,
            price,
            quantity,
            description,
            image,
            category_id
        ) VALUES (%s, %s, %s, %s, %s, %s)''', (title, price, quantity, description, image, category_id))
        connect.commit()
        return 200
    except Exception as error:
        print(error)
        return 404


def update_product(product_id: int, title: str, price: float,
                   quantity: int, description: str, image: str, category_id: int) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('''
            UPDATE products SET 
            product_id = %s,
            title = %s,
            price = %s,
            quantity = %s,
            description = %s,
            image = %s,
            category_id = %s
            WHERE category_id = %s
        ''', (product_id, title, price, quantity, description, image, category_id))
        connect.commit()

        return 200
    except Exception as error:
        print(error)
        return 404


def delete_product(id_product: int) -> int:
    connect, cursor = connect_db()

    try:
        cursor.execute('DELETE FROM products WHERE product_id = %s', (id_product, ))
        connect.commit()

        return 200
    except Exception as error:
        print(error)
        return 404
