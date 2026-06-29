class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        anagram_map = collections.defaultdict(list)
        
        for s in strs:
            # 创建一个长度为 26 的数组统计词频
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # 将列表转换为元组作为字典的键
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())