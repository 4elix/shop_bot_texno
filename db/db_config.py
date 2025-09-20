import psycopg2


def connect_db() -> list:
    connect = psycopg2.connect(
        database='shop_texno',
        password='123',
        user='postgres',
        host='localhost'
    )
    cursor = connect.cursor()

    return [connect, cursor]

