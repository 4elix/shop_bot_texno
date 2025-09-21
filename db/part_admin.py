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
