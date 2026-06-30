class Solution:
    def trap(self, height: List[int]) -> int:
        #对于某个位置，它左侧的最高和右侧的最高决定了这个位置能存多少水
        #维护l，r两个指针，不能确定中间的，只能确定l左和r右的状态
        #那l，r什么时候移动呢？
        area = 0
        l=0
        hl=height[l]
        r=len(height)-1
        hr=height[r]
        while l<r:
            if hl<hr:
                cl = l+1
                hcl=height[cl]
                while hcl<hl:
                    area += hl-hcl
                    cl+=1
                    hcl = height[cl]
                l=cl
                hl=hcl
            else:
                cr = r-1
                hcr=height[cr]
                while hcr<hr:
                    area += hr-hcr
                    cr-=1
                    hcr = height[cr]
                r=cr
                hr=hcr
        return area