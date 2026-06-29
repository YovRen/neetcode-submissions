class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 用列表推导式过滤，并统一转小写
        cleaned = [c.lower() for c in s if c.isalnum()]
        # 直接比较正序列表和反序列表
        return cleaned == cleaned[::-1]
        