# 檔案名稱：order_manager/models/database.py
# 資料庫管理

import sqlite3

class Database:
    def __init__(self, db_name="orders.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # 建立訂單資料表
        query = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_id TEXT NOT NULL,
            invoice_id TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            total REAL NOT NULL
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def get_last_order_id(self):
        # 獲取最後一個訂單編號
        query = "SELECT order_id FROM orders ORDER BY id DESC LIMIT 1"
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None

    def add_order(self, order_id, invoice_id, customer_name, item, quantity, price):
        # 計算總價
        total = quantity * price
        # 新增訂單到資料庫
        query = "INSERT INTO orders (order_id, invoice_id, customer_name, item, quantity, price, total) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (order_id, invoice_id, customer_name, item, quantity, price, total))
        self.conn.commit()

    def get_orders_by_customer(self, customer_name):
        # 根據客戶名稱獲取訂單
        query = "SELECT order_id, invoice_id, item, quantity, price, total FROM orders WHERE customer_name = ?"
        cursor = self.conn.execute(query, (customer_name,))
        orders = cursor.fetchall()
        return [{"order_id": row[0], "invoice_id": row[1], "item": row[2], "quantity": row[3], "price": row[4], "total": row[5]} for row in orders]