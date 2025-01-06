from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設置主視窗
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設置垂直佈局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # 添加標籤
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        # 添加輸入框
        self.stockTickerInput = QtWidgets.QLineEdit(self.centralwidget)
        self.stockTickerInput.setObjectName("stockTickerInput")
        self.verticalLayout.addWidget(self.stockTickerInput)
        
        # 添加按鈕
        self.addStockButton = QtWidgets.QPushButton(self.centralwidget)
        self.addStockButton.setObjectName("addStockButton")
        self.verticalLayout.addWidget(self.addStockButton)
        
        # 添加表格
        self.portfolioTable = QtWidgets.QTableWidget(self.centralwidget)
        self.portfolioTable.setObjectName("portfolioTable")
        self.portfolioTable.setColumnCount(5)
        self.portfolioTable.setHorizontalHeaderLabels(["股票代碼", "股數", "購買價格", "現價", "貨幣"])
        self.verticalLayout.addWidget(self.portfolioTable)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設置 UI 元件的文本
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "投資追蹤器"))
        self.label.setText(_translate("MainWindow", "投資追蹤器"))
        self.stockTickerInput.setPlaceholderText(_translate("MainWindow", "輸入股票代碼"))
        self.addStockButton.setText(_translate("MainWindow", "添加股票"))