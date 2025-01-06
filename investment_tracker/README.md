# Investment Tracker

這是一個使用 PyQt6 構建的個人投資管理工具，功能包括追蹤投資組合和計算盈虧。該專案使用 Pandas 和 yfinance 套件來處理數據。

## 功能

- 追蹤投資組合
- 計算投資組合的總價值
- 獲取即時股票價格

## 安裝

請按照以下步驟來安裝和運行此專案：

1. **克隆專案**：
    ```sh
    git clone https://github.com/yourusername/investment-tracker.git
    cd investment-tracker
    ```

2. **安裝 Poetry**：
    如果還沒有安裝 Poetry，可以使用以下命令安裝：
    ```sh
    pip install poetry
    ```

3. **初始化 Poetry 專案**：
    在專案目錄中運行以下命令來初始化 Poetry：
    ```sh
    poetry install
    ```

4. **轉換 .ui 文件**：
    確保 `tracker_window.ui` 文件已經轉換為 Python 文件。如果還沒有轉換，可以使用以下命令：
    ```sh
    pyuic6 -o ui/ui_tracker_window.py ui/tracker_window.ui
    ```

## 使用

使用以下命令來啟動應用程式：
```sh
poetry run python main.py