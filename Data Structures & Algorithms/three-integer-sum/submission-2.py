class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dict_ = set()
        res = []
        for i, num in enumerate(nums):
            if num not in dict_:
                res_ = self.twoSum(nums[i+1:],-num)
                res.extend([res__+[num] for res__ in res_])
            dict_.add(num)
        return res

    def twoSum(self, nums, target):
        dict_ = set()
        res = []
        for num in nums:
            if target-num in dict_:
                res.append([num,target-num])
            else:
                dict_.add(num)
        return res