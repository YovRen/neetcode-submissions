from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # @cache 自动为你做了这半截事：
        # 如果 amount 以前算过了，直接返回之前存的答案，不再往下执行！
        @cache 
        def dfs(rem):
            if rem < 0: return -1
            if rem == 0: return 0
            
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
                    
            return min_cost if min_cost != float('inf') else -1
            
        return dfs(amount)