class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        while len(nums)>0:
            start = end = num = list(nums)[0]
            nums.remove(num)
            while num-1 in nums:
                start = num-1
                nums.remove(num-1)
                num-=1
            while num+1 in nums:
                end = num+1
                nums.remove(num+1)
                num+=1
            print(end,start)
            length = end-start+1
            max_length = max(max_length,length)
        return max_length