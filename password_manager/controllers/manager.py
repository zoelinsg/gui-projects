# 更新密碼管理邏輯，加入強度檢查

from controllers.generator import PasswordGenerator
from models.database import Database
from models.encryption import Encryption
from controllers.password_checker import PasswordChecker
from cryptography.fernet import Fernet  # 確保正確導入 Fernet

class PasswordManager:
    def __init__(self):
        self.db = Database()
        self.encryption = Encryption(self.load_key())
        self.password_checker = PasswordChecker()
        self.generator = PasswordGenerator()
        
    def save_password(self, account, password):
        # 密碼強度檢查
        result = self.password_checker.check_strength(password)
        if result["strength"] < 0.5:
            return f"密碼過於弱：{result['message']}"
        
        # 儲存密碼
        encrypted_password = self.encryption.encrypt(password)
        self.db.add_password(account, encrypted_password)
        return "密碼已成功保存！"

    def retrieve_password(self, account):
        # 從資料庫中檢索並解密密碼
        encrypted_password = self.db.get_password(account)
        if encrypted_password:
            try:
                return self.encryption.decrypt(encrypted_password)
            except Exception as e:
                return f"解密失敗：{str(e)}"
        return "未找到密碼"

    def generate_password(self, length=12, include_upper=True, include_numbers=True, include_special=True):
        self.generator.length = length
        self.generator.include_upper = include_upper
        self.generator.include_numbers = include_numbers
        self.generator.include_special = include_special
        return self.generator.generate()

    def load_key(self):
        # 假設密鑰存儲在一個文件中
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
            return key