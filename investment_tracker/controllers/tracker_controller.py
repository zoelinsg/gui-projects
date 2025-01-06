from models.stock_data import StockData
from models.portfolio import Portfolio

class TrackerController:
    def __init__(self):
        # 初始化投資組合
        self.portfolio = Portfolio()

    def add_stock_to_portfolio(self, ticker, shares, purchase_price):
        # 獲取當前股票價格和貨幣
        current_price, currency = StockData.get_stock_price_and_currency(ticker)
        # 新增股票到投資組合
        self.portfolio.add_stock(ticker, shares, purchase_price, current_price, currency)