class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #维护一个窗口(l，r】，窗口里必须是不重复
        #怎么保证不重复？拿一个dict（不能有count》1的情况，否则就l右移）
        l=r=0
        char_dict = defaultdict(int)
        max_len = 0
        while r<len(s):
            # s[l+1:r+1]
            #先判断是否满足条件
            char_dict[s[r]]+=1
            while max(list(char_dict.values()))>1:
                char_dict[s[l]]-=1
                l+=1
            #肯定满足条件
            max_len = max(max_len,r-l+1)
            r+=1
        return max_len
