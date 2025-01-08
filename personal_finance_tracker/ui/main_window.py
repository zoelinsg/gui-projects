# src/ui/main_window.py
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QCalendarWidget, QTableWidget, QTableWidgetItem, QLineEdit, QHBoxLayout, QLabel, QComboBox
from db.database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("個人收支追蹤應用")

        self.db = Database()

        # 記錄收支按鈕
        add_button = QPushButton("記錄收支")
        add_button.clicked.connect(self.add_transaction)

        # 刪除收支按鈕
        delete_button = QPushButton("刪除收支")
        delete_button.clicked.connect(self.delete_transaction)

        # 修改收支按鈕
        update_button = QPushButton("修改收支")
        update_button.clicked.connect(self.update_transaction)

        # 查看收支按鈕
        view_button = QPushButton("查看收支")
        view_button.clicked.connect(self.view_transactions)

        # 匯出報表按鈕
        export_button = QPushButton("匯出報表")
        export_button.clicked.connect(self.export_report)

        # 日期選擇器
        self.calendar = QCalendarWidget()

        # 輸入框
        self.amount_input = QLineEdit()
        self.category_input = QLineEdit()
        self.description_input = QLineEdit()
        self.type_input = QComboBox()
        self.type_input.addItems(["INCOME", "EXPENSE"])

        # 記錄表格
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "日期", "金額", "類別", "描述", "類型"])

        # 佈局
        layout = QVBoxLayout()
        layout.addWidget(self.calendar)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("金額:"))
        input_layout.addWidget(self.amount_input)
        input_layout.addWidget(QLabel("類別:"))
        input_layout.addWidget(self.category_input)
        input_layout.addWidget(QLabel("描述:"))
        input_layout.addWidget(self.description_input)
        input_layout.addWidget(QLabel("類型:"))
        input_layout.addWidget(self.type_input)
        layout.addLayout(input_layout)

        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(update_button)
        layout.addWidget(view_button)
        layout.addWidget(export_button)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_transaction(self):
        # 新增交易記錄的邏輯
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        amount = float(self.amount_input.text())
        category = self.category_input.text()
        description = self.description_input.text()
        transaction_type = self.type_input.currentText()
        self.db.add_transaction(date, amount, category, description, transaction_type)
        self.view_transactions()

    def delete_transaction(self):
        # 刪除交易記錄的邏輯
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            transaction_id = int(self.table.item(selected_row, 0).text())
            self.db.delete_transaction(transaction_id)
            self.view_transactions()

    def update_transaction(self):
        # 修改交易記錄的邏輯
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            transaction_id = int(self.table.item(selected_row, 0).text())
            date = self.calendar.selectedDate().toString("yyyy-MM-dd")
            amount = float(self.amount_input.text())
            category = self.category_input.text()
            description = self.description_input.text()
            transaction_type = self.type_input.currentText()
            self.db.update_transaction(transaction_id, date, amount, category, description, transaction_type)
            self.view_transactions()

    def view_transactions(self):
        # 查看交易記錄的邏輯
        transactions = self.db.view_transactions()
        self.table.setRowCount(len(transactions))
        for row_idx, transaction in enumerate(transactions):
            for col_idx, item in enumerate(transaction):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

    def export_report(self):
        # 匯出報表的邏輯
        from reports.report_generator import generate_monthly_report
        generate_monthly_report("finance_tracker.db")