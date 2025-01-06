import pandas as pd
import sqlite3
from models.stock_data import StockData

class Portfolio:
    def __init__(self, db_path="portfolio.db"):
        # 初始化資料庫連接
        self.conn = sqlite3.connect(db_path)
        self.create_table()
        self.load_holdings()

    def create_table(self):
        # 創建持有股票的資料表
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS holdings (
                    id INTEGER PRIMARY KEY,
                    ticker TEXT,
                    shares INTEGER,
                    purchase_price REAL,
                    current_price REAL,
                    currency TEXT
                )
            """)

    def load_holdings(self):
        # 從資料庫加載持有股票
        self.holdings = pd.read_sql_query("SELECT * FROM holdings", self.conn)

    def add_stock(self, ticker, shares, purchase_price, current_price, currency):
        # 新增股票到持有資料框和資料庫
        new_stock = pd.DataFrame([{
            "ticker": ticker,
            "shares": shares,
            "purchase_price": purchase_price,
            "current_price": current_price,
            "currency": currency
        }])
        if self.holdings.empty:
            self.holdings = new_stock
        else:
            self.holdings = pd.concat([self.holdings, new_stock], ignore_index=True)
        with self.conn:
            self.conn.execute("""
                INSERT INTO holdings (ticker, shares, purchase_price, current_price, currency)
                VALUES (?, ?, ?, ?, ?)
            """, (ticker, shares, purchase_price, current_price, currency))

    def calculate_portfolio_value(self):
        # 計算投資組合的總價值
        self.update_current_prices()  # 更新現價
        return sum(self.holdings["shares"] * self.holdings["current_price"])

    def update_current_prices(self):
        # 更新每支股票的現價
        for index, row in self.holdings.iterrows():
            ticker = row["ticker"]
            current_price, currency = StockData.get_stock_price_and_currency(ticker)
            self.holdings.at[index, "current_price"] = current_price
            with self.conn:
                self.conn.execute("""
                    UPDATE holdings
                    SET current_price = ?
                    WHERE ticker = ?
                """, (current_price, ticker))