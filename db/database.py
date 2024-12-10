# Импортирование библиотек
import psycopg2
from config import host, user, password, db_name

# Класс для соединения с базой данных
class Database:
    def __init__(self):
        self.connection = self.connect_db()

    # Функция подключения к БД
    def connect_db(self):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            return connection
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

        db = Database()