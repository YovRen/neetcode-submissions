class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #win容忍的是替换k后只有一种字符的substr
        #判断方式，win中max_count>=total_count-k
        win = defaultdict(int)
        l=0
        max_len=0
        for r,char in enumerate(s):
            win[char]+=1
            while l<=r and max(win.values())+k<sum(win.values()):
                win[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len