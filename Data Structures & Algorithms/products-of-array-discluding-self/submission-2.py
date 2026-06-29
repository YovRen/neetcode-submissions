class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums and nums.index(0)==nums.index(0,-1):
            mul_ = 1
            for num in nums:
                if num!=0:
                    mul_*=num
            res = [0]*len(nums)
            res[nums.index(0)]=mul_
            return res
        elif 0 in nums:
            res = [0]*len(nums)
            return res 
        else:
            mul_ = 1
            for num in nums:
                mul_*=num
            res = [int(mul_/num) for num in nums]
            return res