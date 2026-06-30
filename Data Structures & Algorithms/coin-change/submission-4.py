class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 代表凑齐金额 i 需要的最少硬币数
        # 初始化为无穷大，长度为 amount + 1
        dp = [float('inf')] * (amount + 1)
        
        # base case：凑齐 0 元需要 0 个硬币 (对应你代码的 if amount == 0: return 0)
        dp[0] = 0
        
        # 从金额 1 一直算到 amount
        for i in range(1, amount + 1):
            for coin in coins:
                # 只有当硬币面值小于等于当前要凑的金额时，才能用这枚硬币
                # (对应你代码的 if amount < 0: return -1)
                if i - coin >= 0:
                    # 核心公式：这完全就是你写的 min_cost = min(min_cost, ret + 1)
                    # 要么不选这个硬币（保持原样 dp[i]）
                    # 要么选这个硬币（花费1枚硬币 + 凑齐 i-coin 已经算出的最少硬币数）
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return dp[amount] if dp[amount] != float('inf') else -1