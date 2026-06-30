class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_ = 10000
        max_ = 0
        for num in prices:
            max_ = max(num-min_,max_)
            min_ = min(num,min_)
        return max_