from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = Counter(s1)
        window = Counter()
        
        for i, char in enumerate(s2):
            # 1. 右侧吃进一个字符
            window[char] += 1
            
            # 2. 如果窗口超长了，左侧强制吐出一个字符
            if i >= k:
                left_char = s2[i - k]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char] # 保持字典干净
            
            # 3. 只要窗口里的统计结果和 s1 相同，直接返回 True
            if window == target:
                return True
                
        return False