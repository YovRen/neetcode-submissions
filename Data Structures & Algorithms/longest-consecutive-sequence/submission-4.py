class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1. 先set再升序，2,3,4,5,10,20
        #2. 错位哈。   ，3,4,5,10,20
        #3. 找最长的1序列 1,1,1,5,10
        nums = set(nums)
        max_length = 0
        while len(nums)>0:
            start = end = num = list(nums)[0]
            while num-1 in nums:
                start = num-1
                nums.remove(num-1)
                num-=1
            while num+1 in nums:
                end = num+1
                nums.remove(num+1)
                num+=1
            length = end-start+1
            max_length = max(max_length,length)
        return max_length