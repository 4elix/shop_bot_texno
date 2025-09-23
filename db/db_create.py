try:
    from .db_config import connect_db
except:
    from db_config import connect_db


def create_main_table() -> None:
    connect, cursor = connect_db()
    cursor.execute('''
        DROP TABLE IF EXISTS users CASCADE;
        DROP TABLE IF EXISTS categories CASCADE;
        DROP TABLE IF EXISTS products CASCADE;
        
        CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_name TEXT,
            is_admin BOOLEAN,
            tg_id BIGINT NOT NULL UNIQUE
        );
        
        CREATE TABLE IF NOT EXISTS categories(
            category_id SERIAL PRIMARY KEY,
            category_name TEXT
        );
        
        CREATE TABLE IF NOT EXISTS products(
            product_id SERIAL PRIMARY KEY,
            title TEXT,
            price FLOAT,
            quantity INTEGER,
            description TEXT,
            image TEXT,
            category_id INTEGER REFERENCES categories(category_id) 
        );
    ''')
    connect.commit()


# create_main_table()
