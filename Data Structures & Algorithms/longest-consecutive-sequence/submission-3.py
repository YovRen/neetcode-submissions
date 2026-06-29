class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1. 先set再升序，2,3,4,5,10,20
        #2. 错位哈。   ，3,4,5,10,20
        #3. 找最长的1序列 1,1,1,5,10
        if nums==[]:
            return 0
        nums = sorted(set(nums))
        ones = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        max_count_1 = 0
        count_1 = 0
        for num in ones:
            if num!=1:
                max_count_1 = max(max_count_1,count_1)
                count_1=0
            else:
                count_1+=1
        max_count_1 = max(max_count_1,count_1)
        return max_count_1+1
