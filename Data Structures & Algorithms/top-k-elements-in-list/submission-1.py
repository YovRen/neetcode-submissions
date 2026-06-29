class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num]+=1
        num_count = sorted(num_count.items(), key=lambda x:x[1], reverse=True)
        return [num[0] for num in num_count[:k]]