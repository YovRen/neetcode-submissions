class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = nums.index(target-nums[i])
            if j>=0:
                return [i,j]
