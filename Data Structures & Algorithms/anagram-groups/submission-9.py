class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sps = [(s,''.join(sorted(s))) for s in strs]
        s_dict = defaultdict(list)
        for s1,s2 in sps:
            s_dict[s2].append(s1)
        return s_list.values()

