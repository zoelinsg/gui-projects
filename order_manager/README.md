# 訂單管理系統

這是一個使用 PyQt6 和 SQLite3 開發的簡單訂單管理系統。用戶可以新增訂單並生成發票。

## 功能

- 新增訂單
- 生成發票

## 安裝

1. 安裝 [Poetry](https://python-poetry.org/):
    ```sh
    pip install poetry
    ```

2. 初始化專案：
    ```sh
    poetry install
    ```

3. 進入虛擬環境：
    ```sh
    poetry shell
    ```

## 使用

1. 刪除現有的資料庫檔案（如果存在）：
    ```sh
    rm orders.db
    ```

2. 運行主程式：
    ```sh
    python order_manager/main.py
    ```

## 依賴

- PyQt6
- reportlab
- sqlite3
