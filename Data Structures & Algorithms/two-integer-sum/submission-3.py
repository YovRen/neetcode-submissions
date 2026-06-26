class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) -1): 
            # inner loop smaller list index [i+1->length] (only forgot i+1 here in initial solution!)
            for j in range (i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    # return indexes if they equal target
                    return [i, j]
