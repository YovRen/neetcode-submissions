class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #维护一个窗口，窗口内是s1的子集
        #用一个set来做
        target = dict(Counter(s1))
        l=0
        for r,char in enumerate(s2):
            if char not in target:
                l=r+1
            elif target[char]==0:
                while s2[l-1]!=char:
                    target[s2[l]]+=1
                    l+=1
            else:
                target[char]-=1
            if sum(target.values())==0:
                return True
        return False