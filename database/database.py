import sqlite3

class Database:
    def __init__(self, db_name="memory_assistant.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            encoding BLOB NOT NULL,
            notes TEXT
        )
        ''')
        self.conn.commit()

    def store_notes(self, name, notes):
        self.cursor.execute('''
        INSERT INTO faces (name, notes) VALUES (?, ?)
        ''', (name, notes))
        self.conn.commit()

    def retrieve_notes(self, name):
        self.cursor.execute('''
        SELECT notes FROM faces WHERE name = ?
        ''', (name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.conn.close()