try:
    from .db_config import connect_db
except:
    from db_config import connect_db


def check_register_user(tg_id: int) -> int:
    connect, cursor = connect_db()

    cursor.execute('SELECT * FROM users WHERE tg_id = %s', (tg_id,))
    user = cursor.fetchone()
    if user is None:
        return 404
    else:
        return user


def save_user(user_name: str, is_admin: bool, tg_id: int) -> None:
    connect, cursor = connect_db()

    cursor.execute('INSERT INTO users(user_name, is_admin, tg_id) VALUES(%s, %s, %s)', (user_name, is_admin, tg_id))
    connect.commit()


def get_status_admin(tg_id: int) -> tuple:
    connect, cursor = connect_db()

    cursor.execute('SELECT is_admin FROM users WHERE tg_id = %s', (tg_id, ))
    user = cursor.fetchone()
    return user
