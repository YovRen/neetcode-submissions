class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # 初始化全局最大值
        res = nums[0]
        
        # 记录走到当前位置时的最大值和最小值
        cur_max = nums[0]
        cur_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 因为 cur_max 和 cur_min 在计算时会相互依赖，
            # 需要先把上一轮的 cur_max 存个临时变量，防止被提前覆盖
            temp_max = cur_max
            
            # 核心状态转移：当前最大值，只能从三个候选人中产生
            cur_max = max(num, temp_max * num, cur_min * num)
            
            # 核心状态转移：当前最小值，也只能从三个候选人中产生
            cur_min = min(num, temp_max * num, cur_min * num)
            
            # 随时更新全局最大答案
            res = max(res, cur_max)
            
        return res