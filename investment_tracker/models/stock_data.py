import yfinance as yf

class StockData:
    @staticmethod
    def get_stock_price_and_currency(ticker):
        # 獲取指定股票的即時價格和貨幣
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")
        if history.empty:
            raise ValueError(f"無法獲取股票代碼 {ticker} 的歷史數據")
        price = history['Close'].iloc[0]
        currency = stock.info.get('currency', 'USD')  # 確保有默認貨幣
        return price, currency