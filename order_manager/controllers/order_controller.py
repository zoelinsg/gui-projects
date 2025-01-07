# 檔案名稱：order_manager/controllers/order_controller.py
# 訂單邏輯控制

import random
import string
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from models.database import Database
from models.invoice_generator import InvoiceGenerator

class OrderController(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/order_window.ui", self)
        self.database = Database()
        self.invoice_generator = InvoiceGenerator()

        # 綁定按鈕事件
        self.add_order_button.clicked.connect(self.add_order)
        self.generate_invoice_button.clicked.connect(self.generate_invoice)

    def generate_order_id(self):
        # 生成訂單編號，格式為 S+九位數字
        last_order_id = self.database.get_last_order_id()
        if last_order_id:
            new_id = int(last_order_id[1:]) + 1
        else:
            new_id = 1
        return f"S{new_id:09d}"

    def generate_invoice_id(self):
        # 生成發票編號，格式為 兩位英文+八位數字
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=8))
        return f"{letters}{numbers}"

    def add_order(self):
        # 獲取輸入框的值
        customer_name = self.customer_name_input.text()
        item = self.item_input.text()
        quantity = int(self.quantity_input.text())
        price = float(self.price_input.text())
        
        # 生成訂單編號和發票編號
        order_id = self.generate_order_id()
        invoice_id = self.generate_invoice_id()
        
        # 新增訂單到資料庫
        self.database.add_order(order_id, invoice_id, customer_name, item, quantity, price)
        QMessageBox.information(self, "成功", "訂單新增成功！")

    def generate_invoice(self):
        # 獲取客戶名稱
        customer_name = self.customer_name_input.text()
        # 從資料庫獲取客戶的所有訂單
        orders = self.database.get_orders_by_customer(customer_name)
        if orders:
            # 使用第一個訂單的發票號碼
            invoice_id = orders[0]['invoice_id']
            # 生成發票
            self.invoice_generator.generate(invoice_id, customer_name, orders)
            QMessageBox.information(self, "成功", "發票生成成功！")
        else:
            QMessageBox.warning(self, "錯誤", "沒有找到該客戶的訂單！")