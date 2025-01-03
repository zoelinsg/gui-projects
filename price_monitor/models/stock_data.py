import yfinance as yf
import logging

# 設置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StockData:
    def __init__(self, ticker: str):
        # 初始化股票數據類別，設置股票代碼
        self.ticker = ticker

    def get_latest_price(self):
        # 獲取最新的股票價格
        try:
            stock = yf.Ticker(self.ticker)
            data = stock.history(period="1d")
            if data.empty:
                raise ValueError(f"No data found for ticker {self.ticker}")
            return data['Close'].iloc[-1]
        except Exception as e:
            logger.error(f"Error fetching latest price for {self.ticker}: {e}")
            raise

    def get_currency(self):
        # 獲取股票的貨幣
        try:
            stock = yf.Ticker(self.ticker)
            info = stock.info
            return info.get('currency', 'Unknown')
        except Exception as e:
            logger.error(f"Error fetching currency for {self.ticker}: {e}")
            raise

    def get_stock_info(self):
        # 獲取更多股票資訊
        try:
            stock = yf.Ticker(self.ticker)
            data = stock.history(period="1d")
            if data.empty:
                raise ValueError(f"No data found for ticker {self.ticker}")
            info = stock.info
            return {
                'open': data['Open'].iloc[-1],
                'high': data['High'].iloc[-1],
                'low': data['Low'].iloc[-1],
                'volume': data['Volume'].iloc[-1],
                'currency': info.get('currency', 'Unknown')
            }
        except ValueError as ve:
            logger.error(f"ValueError fetching stock info for {self.ticker}: {ve}")
            raise
        except Exception as e:
            logger.error(f"Error fetching stock info for {self.ticker}: {e}")
            raise

    def get_stock_history(self, period="1mo"):
        # 獲取股票歷史數據
        try:
            stock = yf.Ticker(self.ticker)
            data = stock.history(period=period)
            if data.empty:
                raise ValueError(f"No data found for ticker {self.ticker}")
            return data
        except Exception as e:
            logger.error(f"Error fetching stock history for {self.ticker}: {e}")
            raise