# src/reports/report_generator.py
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

def generate_monthly_report(db_path):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    
    # 生成每月支出報表
    monthly_summary = df.groupby("category")["amount"].sum()
    print(monthly_summary)

    # 繪製每月支出報表
    plt.figure(figsize=(10, 5))
    monthly_summary.plot(kind="bar")
    plt.title("monthly expense report")
    plt.show()

    # 匯出報表到 Excel
    df.to_excel("monthly_report.xlsx", index=False)