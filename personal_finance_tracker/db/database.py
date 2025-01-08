# src/db/database.py
import sqlite3

class Database:
    def __init__(self, db_name="finance_tracker.db"):
        # 連接到 SQLite 資料庫
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # 建立 transactions 表格
        query = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT,
            type TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_transaction(self, date, amount, category, description, transaction_type):
        # 新增一筆交易記錄
        query = "INSERT INTO transactions (date, amount, category, description, type) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (date, amount, category, description, transaction_type))
        self.conn.commit()

    def delete_transaction(self, transaction_id):
        # 刪除一筆交易記錄
        query = "DELETE FROM transactions WHERE id = ?"
        self.conn.execute(query, (transaction_id,))
        self.conn.commit()

    def update_transaction(self, transaction_id, date, amount, category, description, transaction_type):
        # 修改一筆交易記錄
        query = """
        UPDATE transactions
        SET date = ?, amount = ?, category = ?, description = ?, type = ?
        WHERE id = ?
        """
        self.conn.execute(query, (date, amount, category, description, transaction_type, transaction_id))
        self.conn.commit()

    def view_transactions(self):
        # 查看所有交易記錄
        query = "SELECT * FROM transactions"
        cursor = self.conn.execute(query)
        return cursor.fetchall()