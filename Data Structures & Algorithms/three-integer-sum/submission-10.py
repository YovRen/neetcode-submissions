class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(len(nums) - 2):
            # 1. 外层去重：只看有序数组的特性，抛弃额外的 dict_ 集合
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 2. 传递起始下标 i+1，彻底消灭数组切片！
            # 找到的所有两数之和，直接跟 nums[i] 组装
            res_ = self.twoSum(nums, i + 1, -nums[i])
            res.extend(res_)
            
        return res

    # 改造后的 twoSum：接收原始数组和起始位置
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        seen = set()
        res = []
        
        # 只需要遍历一次
        i = start
        while i < len(nums):
            num = nums[i]
            complement = target - num
            
            if complement in seen:
                res.append([-target, complement, num])
                
                # 3. 内层去重：既然找到了一个答案，且数组是有序的，
                # 把后面所有相同的数字直接跳过，这比你那串复杂的 if 优雅一万倍！
                while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                    
            seen.add(num)
            i += 1
            
        return res