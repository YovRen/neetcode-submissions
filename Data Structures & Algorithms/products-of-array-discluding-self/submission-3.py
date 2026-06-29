class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_0  = len([num for num in nums if num==0])
        if count_0==1:
            mul_ = 1
            for num in nums:
                if num!=0:
                    mul_*=num
            res = [0]*len(nums)
            res[nums.index(0)]=mul_
            return res
        elif count_0>1:
            res = [0]*len(nums)
            return res 
        else:
            mul_ = 1
            for num in nums:
                mul_*=num
            res = [int(mul_/num) for num in nums]
            return res