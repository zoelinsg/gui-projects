# 密碼生成邏輯

import random
import string

class PasswordGenerator:
    def __init__(self, length=12, include_upper=True, include_numbers=True, include_special=True):
        self.length = length
        self.include_upper = include_upper
        self.include_numbers = include_numbers
        self.include_special = include_special

    def generate(self):
        characters = string.ascii_lowercase
        if self.include_upper:
            characters += string.ascii_uppercase
        if self.include_numbers:
            characters += string.digits
        if self.include_special:
            characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

        if len(characters) < self.length:
            raise ValueError("可用字符數不足以生成所需長度的密碼")

        return ''.join(random.choice(characters) for _ in range(self.length))