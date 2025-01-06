import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_tracker_window import Ui_MainWindow  # 引入轉換後的 UI 文件
from controllers.tracker_controller import TrackerController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # 初始化主視窗
        super().__init__()
        self.setupUi(self)
        self.controller = TrackerController()
        
        # 設置按鈕點擊事件
        self.addStockButton.clicked.connect(self.add_stock)
        
        # 加載投資組合表格
        self.update_portfolio_table()

    def add_stock(self):
        # 獲取輸入的股票代碼
        ticker = self.stockTickerInput.text()
        if not ticker:
            QMessageBox.warning(self, "輸入錯誤", "請輸入股票代碼")
            return
        
        # 假設每次添加 10 股，購買價格為 100
        shares = 10
        purchase_price = 100
        
        try:
            self.controller.add_stock_to_portfolio(ticker, shares, purchase_price)
            QMessageBox.information(self, "成功", f"已成功添加股票 {ticker}")
            self.update_portfolio_table()
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"添加股票失敗: {e}")

    def update_portfolio_table(self):
        # 更新投資組合表格
        self.portfolioTable.setRowCount(len(self.controller.portfolio.holdings))
        for row_index, row_data in self.controller.portfolio.holdings.iterrows():
            self.portfolioTable.setItem(row_index, 0, QTableWidgetItem(row_data["ticker"]))
            self.portfolioTable.setItem(row_index, 1, QTableWidgetItem(str(row_data["shares"])))
            self.portfolioTable.setItem(row_index, 2, QTableWidgetItem(f"{row_data['purchase_price']}"))
            self.portfolioTable.setItem(row_index, 3, QTableWidgetItem(f"{row_data['current_price']}"))
            self.portfolioTable.setItem(row_index, 4, QTableWidgetItem(row_data["currency"]))

if __name__ == "__main__":
    # 啟動應用程式
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # 顯示主視窗
    sys.exit(app.exec())  # 執行應用程式主迴圈