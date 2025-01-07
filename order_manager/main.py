# 檔案名稱：order_manager/main.py
# 主程式入口

from PyQt6.QtWidgets import QApplication
from controllers.order_controller import OrderController

import sys

def main():
    # 創建應用程式實例
    app = QApplication(sys.argv)
    # 創建主視窗
    window = OrderController()
    window.show()
    # 執行應用程式
    sys.exit(app.exec())

if __name__ == "__main__":
    main()