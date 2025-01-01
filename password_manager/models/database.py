# 資料庫操作

import sqlite3

class Database:
    def __init__(self, db_path="passwords.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            account TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_password(self, account, password):
        query = "INSERT INTO passwords (account, password) VALUES (?, ?)"
        self.connection.execute(query, (account, password))
        self.connection.commit()

    def get_password(self, account):
        query = "SELECT password FROM passwords WHERE account = ?"
        cursor = self.connection.execute(query, (account,))
        row = cursor.fetchone()
        return row[0] if row else None