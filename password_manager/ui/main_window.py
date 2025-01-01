# 主視窗邏輯

from PyQt6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QSlider, QCheckBox, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from controllers.manager import PasswordManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.manager = PasswordManager()

        # 設置視窗標題
        self.setWindowTitle("密碼管理器")

        # UI 元件
        self.generate_button = QPushButton("生成密碼", self)
        self.password_display = QLineEdit(self)
        self.length_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.length_slider.setMinimum(8)  # 設置滑桿最小值
        self.length_slider.setMaximum(32)  # 設置滑桿最大值
        self.length_slider.setValue(12)  # 設置滑桿初始值
        self.uppercase_checkbox = QCheckBox("包含大寫字母", self)
        self.uppercase_checkbox.setChecked(True)  # 預設勾選
        self.numbers_checkbox = QCheckBox("包含數字", self)
        self.numbers_checkbox.setChecked(True)  # 預設勾選
        self.special_checkbox = QCheckBox("包含特殊字符", self)
        self.special_checkbox.setChecked(True)  # 預設勾選

        # 新增 UI 元件
        self.account_input = QLineEdit(self)
        self.account_input.setPlaceholderText("輸入帳號")
        self.save_button = QPushButton("儲存密碼", self)
        self.retrieve_button = QPushButton("檢索密碼", self)
        self.retrieved_password_display = QLineEdit(self)
        self.retrieved_password_display.setReadOnly(True)
        self.strength_label = QLabel(self)

        # 設置佈局
        layout = QVBoxLayout()
        layout.addWidget(self.length_slider)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.numbers_checkbox)
        layout.addWidget(self.special_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_display)
        layout.addWidget(self.account_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.retrieve_button)
        layout.addWidget(self.retrieved_password_display)
        layout.addWidget(self.strength_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 信號連接
        self.generate_button.clicked.connect(self.generate_password)
        self.save_button.clicked.connect(self.save_password)
        self.retrieve_button.clicked.connect(self.retrieve_password)

    def generate_password(self):
        # 從 UI 獲取策略選項
        length = self.length_slider.value()
        include_upper = self.uppercase_checkbox.isChecked()
        include_numbers = self.numbers_checkbox.isChecked()
        include_special = self.special_checkbox.isChecked()

        # 調用生成邏輯
        password = self.manager.generate_password(length, include_upper, include_numbers, include_special)
        self.password_display.setText(password)

        # 檢查密碼強度
        result = self.manager.password_checker.check_strength(password)
        self.strength_label.setText(f"密碼強度: {result['strength']:.2f} - {result['message']}")

    def save_password(self):
        account = self.account_input.text()
        password = self.password_display.text()
        if account and password:
            message = self.manager.save_password(account, password)
            self.strength_label.setText(message)
        else:
            self.strength_label.setText("請輸入帳號和密碼")

    def retrieve_password(self):
        account = self.account_input.text()
        if account:
            password = self.manager.retrieve_password(account)
            self.retrieved_password_display.setText(password)
        else:
            self.retrieved_password_display.setText("請輸入帳號")