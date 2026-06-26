class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {num:i for i,num in enumerate(nums)}
        for i, num in enumerate(nums):
            j = nums_dict.get(target-num,-1)
            if j>0:
                return [i,j]