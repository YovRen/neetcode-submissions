class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {(s,''.join(sorted(s))) for s in strs}
        print(strs)
        sps = sorted(s_dict,key=lambda x:x[1])
        ress = []
        cur = None
        for s1,s2 in sps:
            if s2 != cur:
                ress.append([s1])
                cur = s2
            else:
                ress[-1].append(s1)
        return ress

