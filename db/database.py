# Импортирование библиотек
import psycopg2
from db import config


# Класс для соединения с базой данных
class Database():
    def __init__(self):
        self.connection = self.connect_db()

    # Функция подключения к БД
    def connect_db(self):
        try:
            connection = psycopg2.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.db_name
            )
            print("Соединение с базой данных установлено")
            return connection
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

    def take_partner_information(self):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT partners_type, partners_name, partners_director, partners_email, partners_phone, partners_ur_adress, partners_inn, partners_rate
            FROM partners_import
            """

            cursor.execute(query)
            partners = [
                {
                    "type": row[0],
                    "name": row[1],
                    "director": row[2],
                    "email": row[3],
                    "phone": row[4],
                    "ur_adress": row[5],
                    "inn": row[6],
                    "rate": row[7]
                }
                for row in cursor.fetchall()
            ]
            cursor.close()
            return partners
        except Exception as e:
            return []

    def sale_sum(self, partners_name : str):
        if not self.connection:
            return []
        try:
            cursor = self.connection.cursor()

            query = f"""
            select sum(partner_products_count)
            from partner_products_import
            where partner_name_fk = '{partners_name}'
            """
            cursor.execute(query, {partners_name})

            sales_data = [
                {
                    "procent": row[0]
                }
                for row in cursor.fetchall()
            ]

            cursor.close()
            return sales_data

        except Exception as e:
            return []