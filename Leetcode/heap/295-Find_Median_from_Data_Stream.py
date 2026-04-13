from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        """Inititalize the data structure here"""
        # Two heaps: Small (maxHeap) and Large (minHeap)
        # Heaps should be equal size or off by one at most
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # Python doesn't have maxheaps, only minheaps, so we get around this by mult by -1
        heapq.heappush(self.small, -1 * num)

        # Problem: Make sure every num in small is <= every num in large, we have this problem is below is True
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Problem: What if the size for self.small is bigger than self.large?
        if len(self.small) > len(self.large) + 1:
            # POP from small, push to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Problem: What if the size for self.large is bigger than self.small?
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # We have an odd number of elements - WITH extra one in self.small
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        # We have an odd number of elemtns - WITH extra one in self.large
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # Even number of elements, take both and get average
        return (-1 * self.small[0] + self.large[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()