try:
    from .db_config import connect_db
except:
    from db_config import connect_db


def get_all_categories():
    connect, cursor = connect_db()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    return categories


def get_names_category():
    connect, cursor = connect_db()

    cursor.execute('SELECT category_name FROM categories')
    names_category = cursor.fetchall()
    return names_category


def get_product_title_for_category(category):
    connect, cursor = connect_db()

    cursor.execute('SELECT category_id FROM categories WHERE category_name = %s', (category, ))
    cat_id = cursor.fetchone()

    cursor.execute('SELECT title FROM products WHERE category_id = %s', (cat_id, ))
    list_titles = [title for title in cursor.fetchall()]
    return list_titles


def get_info_product(title):
    connect, cursor = connect_db()
    try:
        cursor.execute('SELECT * FROM products WHERE title = %s', (title, ))
        product = cursor.fetchone()
        return product
    except Exception as error:
        print(error)
        return 404