import psycopg2

from os import getenv
from dotenv import load_dotenv

load_dotenv()


class PsqlDB:

    def __init__(self):
        self.connect = psycopg2.connect(
            dbname=getenv('DB_NAME'),
            user=getenv('DB_USER'),
            password=getenv('PASSWORD'),
            host=getenv('HOST'),
            port=getenv('PORT')
        )
        self.cursor = self.connect.cursor()

    def execute(self, query):
        with self.connect:
            self.cursor.execute(query)
        return self.cursor

    def fetchone(self, query):
        cursor = self.execute(query)
        return cursor.fetchone()

    def db_save(self, chat_id, lang):
        query = f"""INSERT INTO users (chat_id, lang) VALUES ({chat_id}, '{lang}');"""
        self.execute(query)

    def get_lang(self, chat_id):
        query = f"""SELECT lang FROM users WHERE chat_id={chat_id};"""
        return self.fetchone(query)[0]

    def update_lang(self, chat_id, lang):
        query = f"""UPDATE users SET lang='{lang}' WHERE chat_id={chat_id};"""
        self.execute(query)


pg = PsqlDB()
if __name__ == '__main__':
    # print(getenv('DB_NAME'))
    # print(getenv('DB_USER'))
    # print(getenv('PASSWORD'))
    # print(getenv('HOST'))
    # print(getenv('PORT'))
    pg = PsqlDB()
    # pg.db_save(432472837, 'ru')
    # pg.db_save(232587235, 'ru')
    print(pg.get_lang(42312312))
