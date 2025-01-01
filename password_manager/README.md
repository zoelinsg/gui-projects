# 密碼管理器

這是一個使用 PyQt6 構建的密碼管理器應用程式，具有生成和管理密碼的功能。

## 功能

- 生成隨機密碼
- 檢查密碼強度
- 加密和儲存密碼
- 從資料庫中檢索密碼

password_manager/
├── password_manager/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── generator.py
│   │   ├── manager.py
│   │   └── password_checker.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── encryption.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── main_window.py
│   │   └── main_window.ui
│   ├── main.py
├── pyproject.toml
├── README.md
└── secret.key

檔案功能和設計原理
password_manager/controllers/

__init__.py：初始化控制器模組。
generator.py：包含生成隨機密碼的邏輯。
manager.py：管理密碼的主要邏輯，包括生成、加密、儲存和檢索密碼。
password_checker.py：檢查密碼強度的邏輯。
password_manager/models/

__init__.py：初始化模型模組。
database.py：處理與 SQLite 資料庫的交互，包括創建表格、插入和檢索密碼。
encryption.py：處理密碼的加密和解密。
password_manager/ui/

__init__.py：初始化 UI 模組。
main_window.py：定義主視窗的邏輯，包括 UI 元件的初始化和事件處理。
main_window.ui：定義主視窗的佈局和設計。
password_manager/main.py：應用程式的入口點，啟動 PyQt6 應用程式並顯示主視窗。

pyproject.toml：Poetry 的配置文件，定義了專案的依賴項和其他設置。

README.md：專案的說明文件，包含安裝、使用和打包應用程式的說明。

secret.key：加密密鑰文件，用於加密和解密密碼。

依賴項
PyQt6
cryptography
password-strength
PyInstaller