from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 边界情况防越界
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        # 注意：不要把 nums 作为参数传进去！
        @cache
        def dfs(pos, typ):
            if pos >= n:
                return 0
                
            # 如果到了最后一间房
            if pos == n - 1:
                # 之前偷了第0间(typ==0)，这间不能偷
                # 没偷第0间(typ==1)，这间可以偷
                return 0 if typ == 0 else nums[pos]

            # 核心转移方程你写得极其完美
            return max(nums[pos] + dfs(pos + 2, typ), dfs(pos + 1, typ))

        # 方案一：偷第 0 间房 (typ=0)，那么下一间只能从第 2 间开始看
        rob_first = nums[0] + dfs(2, 0)
        
        # 方案二：不偷第 0 间房 (typ=1)，那么下一间从第 1 间开始，自由选择
        skip_first = dfs(1, 1)
        
        return max(rob_first, skip_first)