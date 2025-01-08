# app.py
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys

def main():
    # 初始化 PyQt 應用程式
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()