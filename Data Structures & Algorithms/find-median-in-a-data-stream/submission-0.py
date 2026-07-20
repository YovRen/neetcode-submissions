import heapq

class MedianFinder:

    def __init__(self):
        self.l_heap = []#大顶堆，push/pop相反数
        self.r_heap = []#小顶堆

    def addNum(self, num: int) -> None:
        # 要决定把num放到左右哪个堆里？
        # 要保证左右的数量相同，所以需要分情况讨论：
        l_cnt = len(self.l_heap)
        r_cnt = len(self.r_heap)
        if l_cnt==0:
            heapq.heappush(self.l_heap,-num)
            return
        elif r_cnt==0:
            heapq.heappush(self.r_heap,num)
            return
        l_max = -self.l_heap[0]
        r_min = self.r_heap[0]
        if l_cnt == r_cnt: #最多只能相差一
            if l_max<=num<=r_min:
                heapq.heappush(self.l_heap,-num)
            elif num<l_max:
                heapq.heappush(self.l_heap,-num)
            else:
                heapq.heappush(self.l_heap,-heappop(self.r_heap))
                heapq.heappush(self.r_heap,num)
        else: # l_cnt==r_cnt+1
            if l_max<=num<=r_min:
                heapq.heappush(self.r_heap,num)
            elif num<l_max:
                heapq.heappush(self.r_heap,-heappop(self.l_heap))
                heapq.heappush(self.l_heap,-num)
            else:
                heapq.heappush(self.r_heap,num)

    def findMedian(self) -> float:
        l_cnt = len(self.l_heap)
        r_cnt = len(self.r_heap)
        if l_cnt==0:
            return -1
        elif r_cnt==0:
            return -self.l_heap[0]
        l_max = -self.l_heap[0]
        r_min = self.r_heap[0]
        if l_cnt == r_cnt: #最多只能相差一
            return (l_max+r_min)/2
        else:
            return l_max