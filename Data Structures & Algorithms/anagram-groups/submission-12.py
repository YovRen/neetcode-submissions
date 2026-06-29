class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = collections.defaultdict(list)
        
        for s in strs:
            # 将排序后的字符串作为 key (tuple或者拼接后的字符串都可以)
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())

