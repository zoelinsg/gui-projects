# 加密邏輯

from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        return self.cipher.decrypt(ciphertext.encode()).decode()