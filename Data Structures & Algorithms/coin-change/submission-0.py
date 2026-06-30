class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<0:
            return -1
        elif amount==0:
            return 0
        min_cost = float('inf')
        for coin in coins:
            ret = self.coinChange(coins, amount-coin)
            if ret != -1:
                min_cost = min(min_cost,ret+1)
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost