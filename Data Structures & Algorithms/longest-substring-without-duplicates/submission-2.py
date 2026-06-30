class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()  # 用来记录窗口内存在的字符
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # 如果即将加入的字符重复了，就不断收缩左边界
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            # 把当前字符加入窗口，并更新最大长度
            window.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len