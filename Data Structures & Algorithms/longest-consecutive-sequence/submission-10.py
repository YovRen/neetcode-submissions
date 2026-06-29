class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        while len(nums)>0:
            start = end = nums.pop()
            while start-1 in nums:
                nums.remove(start-1)
                start-=1
            while end+1 in nums:
                nums.remove(end+1)
                end+=1
            length = end-start+1
            max_length = max(max_length,length)
        return max_length