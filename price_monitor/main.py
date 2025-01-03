import sys
from PyQt6.QtWidgets import QApplication
from ui.monitor_window import MonitorWindow  # 從 monitor_window 模組導入 MonitorWindow 類別

# 主程式入口
if __name__ == "__main__":
    # 創建應用程式實例
    app = QApplication(sys.argv)
    # 創建主視窗實例
    main_window = MonitorWindow()
    # 顯示主視窗
    main_window.show()
    # 啟動應用程式事件循環
    sys.exit(app.exec())