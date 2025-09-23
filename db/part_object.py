try:
    from .db_config import connect_db
except:
    from db_config import connect_db


def get_all_categories():
    connect, cursor = connect_db()
    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()
    return categories

