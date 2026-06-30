class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # 记录字符最后一次出现的下标
        l = 0
        max_len = 0
        
        for r, char in enumerate(s):
            # 如果字符出现过，并且它还在我们的窗口内
            if char in char_index_map and char_index_map[char] >= l:
                # 左指针直接跳到重复字符的上一次位置的下一个！
                l = char_index_map[char] + 1
                
            # 记录/更新当前字符的最新的下标
            char_index_map[char] = r
            
            # 更新最大长度
            max_len = max(max_len, r - l + 1)
            
        return max_len