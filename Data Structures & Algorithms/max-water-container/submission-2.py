class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            # 高度由短板决定
            h = min(height[l], height[r])
            # 更新最大面积
            max_area = max(max_area, h * (r - l))
            
            # 核心贪心逻辑：谁矮，谁往里挪
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area