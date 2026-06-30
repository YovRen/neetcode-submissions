class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        area = 0
        
        while l < r:
            # 动态维护左侧最高和右侧最高
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            
            # 谁矮，说明短板在谁那侧，就可以放心地结算那一侧的水
            if left_max < right_max:
                area += left_max - height[l]
                l += 1
            else:
                area += right_max - height[r]
                r -= 1
                
        return area