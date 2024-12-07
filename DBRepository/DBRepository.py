import sqlite3

class DBRepository:
    def __initDb(self):
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL UNIQUE
)
''')
        self.cursor.execute('''
CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL UNIQUE
)
''')

        # Список ключевых слов
        keywords = [
            'Кимры', 'Кимрский', 'Дубна', 'Талдом', 'Талдомский',
            'Тверь', 'Тверская', 'Калязин', 'Калязинский', 'Кашин',
            'Кашинский', 'Рамешки', 'Рамешковский'
        ]

        # Вставка ключевых слов в таблицу
        for keyword in keywords:
            self.cursor.execute('''
            INSERT OR IGNORE INTO keywords (keyword) VALUES (?)
            ''', (keyword,))

        self.conn.commit()

    def __init__(self, path_to_db):
        self.conn = sqlite3.connect(path_to_db)
        self.cursor = self.conn.cursor()
        self.__initDb()

    def add_keyword(self, keyword):
        self.cursor.execute('''
SELECT 1 FROM keywords WHERE keyword = ?
''', (keyword,))
        if self.cursor.fetchone() is None:
            self.cursor.execute('''
INSERT INTO keywords (keyword) VALUES (?)
''', (keyword,))
            self.conn.commit()
            return True
        else:
            print(f"Ключевое слово '{keyword}' уже существует в базе данных.")
            return False

    def delete_keyword(self, keyword_id):
        # Проверка на существование ключевого слова по id
        self.cursor.execute('''
SELECT 1 FROM keywords WHERE id = ?
''', (keyword_id,))
        if self.cursor.fetchone() is None:
            print(f"Ключевое слово с id '{keyword_id}' не найдено.")
            return False
        self.cursor.execute('''
DELETE FROM keywords WHERE id = ?
''', (keyword_id,))
        self.conn.commit()
        return True

    def get_all_keywords(self):
        self.cursor.execute('''
SELECT * FROM keywords
''')
        return self.cursor.fetchall()
