# 密碼強度檢查邏輯

from password_strength import PasswordPolicy, PasswordStats

# 定義密碼強度檢查策略
class PasswordChecker:
    def __init__(self):
        self.policy = PasswordPolicy.from_names(
            length=8,            # 密碼至少8個字符
            uppercase=1,         # 至少1個大寫字母
            numbers=1,           # 至少1個數字
            special=1,           # 至少1個特殊字符
            nonletters=0         # 非字母字符限制
        )

    def check_strength(self, password):
        stats = PasswordStats(password)
        policy_violations = self.policy.test(password)

        if not policy_violations:
            return {
                "strength": stats.strength(),
                "message": "密碼強度足夠"
            }
        else:
            # 返回所有未通過的檢查項
            violations = [str(v) for v in policy_violations]
            return {
                "strength": stats.strength(),
                "message": f"密碼不符合安全要求：{'，'.join(violations)}"
            }