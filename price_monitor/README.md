# 股票價格查詢應用程式

這個應用程式使用 `yfinance` 庫來查詢股票和加密貨幣的價格。以下是一些常見的股票和加密貨幣代碼：

| 名稱                           | 代碼      |
| ------------------------------ | --------- |
| 蘋果公司（Apple Inc.）         | AAPL      |
| 特斯拉公司（Tesla Inc.）       | TSLA      |
| 台積電（TSMC）                 | 2330.TW   |
| 華碩電腦（ASUSTeK Computer Inc.）| 2357.TW   |
| 比特幣（Bitcoin）              | BTC-USD   |
| 以太坊（Ethereum）             | ETH-USD   |

## 功能說明

- 查詢股票和加密貨幣的最新價格
- 顯示股票的開盤價、最高價、最低價、成交量和貨幣
- 繪製股票價格的歷史圖表

## 安裝

1. 克隆此儲存庫到本地端：
    ```sh
    git clone https://github.com/zoelinsg/gui-projects.git
    cd price_monitor
    ```

2. 使用 `poetry` 安裝依賴：
    ```sh
    poetry install
    ```

## 使用方法

1. 啟動應用程式：
    ```sh
    poetry run python main.py
    ```

2. 在應用程式的輸入框中輸入股票或加密貨幣代碼，然後點擊「獲取價格」按鈕。

## 文件結構

- [main.py](http://_vscodecontentref_/0)：應用程式的入口點
- [stock_data.py](http://_vscodecontentref_/1)：包含獲取股票和加密貨幣數據的邏輯
- [monitor_controller.py](http://_vscodecontentref_/2)：包含與 WebSocket 連接的邏輯
- [ui_monitor_window.py](http://_vscodecontentref_/3)：由 PyQt6 生成的 UI 文件
- [monitor_window.ui](http://_vscodecontentref_/4)：UI 設計文件

## 常見問題

### 為什麼無法查詢到某些股票的價格？

這可能是由於以下原因：
- 股票代碼無效或已退市
- Yahoo Finance 暫時無法提供該股票的數據
- 網絡連接問題

請確認輸入的股票代碼是否正確，並嘗試使用其他有效的股票代碼。

### 如何報告問題？

如果您在使用過程中遇到任何問題，請在 GitHub 儲存庫中創建一個 Issue，並提供詳細的錯誤信息和重現步驟。

## 貢獻

歡迎任何形式的貢獻！請先閱讀 CONTRIBUTING.md 文件了解更多信息。

## 授權

此專案使用 MIT 授權。