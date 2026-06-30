class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #l，r维护一个窗口,左闭右开
        #如果不满足条件就收缩窗口
        l=0
        r=1
        max_len = 1
        while r<len(s):
            while s[r] in s[l:r]:
                l+=1
            r+=1
            max_len=max(max_len,r-l)
        return max_len