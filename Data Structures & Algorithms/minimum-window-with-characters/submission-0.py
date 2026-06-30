class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #维护一个窗口，l r，以r结尾的最短等效字符串
        min_len = float('inf')
        min_len_str = ""
        tar = dict(Counter(t))
        l=0
        for r,char in enumerate(s):
            if char not in tar:
                continue
            tar[char]-=1
            while s[l] not in tar or tar[s[l]]<0:
                l+=1
                if s[l] in tar:
                    tar[s[l]]+= 1
            if all(list(tar.values())<=0):
                min_len=min(min_len,r+1-l)
                min_len_str=s[l:r+1]
        return min_len_str