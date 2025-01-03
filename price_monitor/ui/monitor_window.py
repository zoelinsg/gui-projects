from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.stock_data import StockData
from ui_monitor_window import Ui_MonitorWindow  # 從 ui_monitor_window 模組導入 Ui_MonitorWindow 類別

class MonitorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MonitorWindow()  # 創建 Ui_MonitorWindow 實例
        self.ui.setupUi(self)  # 設置 UI
        
        self.setWindowTitle("股票和虛擬貨幣監控") # 設置窗口標題
        self.setGeometry(100, 100, 800, 600) # 設置窗口大小和位置
        
        # 創建圖表畫布
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.verticalLayout.addWidget(self.canvas)
        
        # 連接按鈕點擊事件到方法
        self.ui.pushButton.clicked.connect(self.display_price)
    
    def display_price(self):
        # 獲取輸入框中的股票代碼
        ticker = self.ui.lineEdit.text()
        # 使用 StockData 類別獲取股票資訊
        stock_data = StockData(ticker)
        try:
            stock_info = stock_data.get_stock_info()
            # 更新標籤顯示股票資訊
            self.ui.label_open.setText(f"開盤價: {stock_info['open']}")
            self.ui.label_high.setText(f"最高價: {stock_info['high']}")
            self.ui.label_low.setText(f"最低價: {stock_info['low']}")
            self.ui.label_volume.setText(f"成交量: {stock_info['volume']}")
            self.ui.label_currency.setText(f"貨幣: {stock_info['currency']}")
            
            # 獲取股票歷史數據並繪製圖表
            stock_history = stock_data.get_stock_history()
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            stock_history['Close'].plot(ax=ax, title=f"{ticker} Stock Price")
            self.canvas.draw()
        except ValueError as e:
            QMessageBox.critical(self, "錯誤", str(e))
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"無法獲取數據: {e}")