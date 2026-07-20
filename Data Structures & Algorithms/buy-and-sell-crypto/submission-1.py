class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #每次到i位置，求i之前的最大res，更新最小值
        maxP = 0
        mini = float('inf')
        for price in prices:
            maxP = max(maxP,price-mini)
            mini = min(mini,price)
        return maxP