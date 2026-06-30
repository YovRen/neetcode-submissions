class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #两个指针l，r，面积（r-l）✖️min(pl,pr)
        #要往里收看有没有更优的选择，收l还是r？，循环：min(l,r)往里找min(l,r)高的停下
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l<r:
            ln = heights[l]
            rn = heights[r]
            area = min(ln,rn)*(r-l)
            maxArea = max(maxArea,area)
            if ln < rn:
                l+=1
                while l < r and heights[l]<ln:
                    l+=1
            else:
                r-=1
                while l < r and heights[r]<rn:
                    r-=1
        return maxArea
