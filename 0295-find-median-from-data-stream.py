"""
solution 1. sort

solution 2.
Max-heap small has the smaller half of the numbers.
Min-heap large has the larger half of the numbers.
This gives me direct access to the one or two middle values (they're the tops of the heaps), so getting the median takes O(1) time. And adding a number takes O(log n) time.


"""

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num): # O(logn)
    	"""
		find the smallest value from large and push to small
		if large has less value, then push from small to large
        len(large) always >= len(small)
    	"""
        small, large = self.heaps
        # push num to large and pop the smallest value of large 
        # heapreplace - pop the smallest value first then push the num
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))
        print("small->", small)
        print("large->", large)
        
    def findMedian(self):  # O(1)
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # print("median: ", (large[0] - small[0]) / 2.0)
        # if len(small) > len(large):  
            # return float(small[0])*(-1)
        return (large[0] - small[0]) / 2.0
    

class MedianFinder:

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap
    
    # Time: O(logn)
    def addNum(self, num: int) -> None:
        # default push to the small first
        heapq.heappush(self.small, (-1) * num)
            
        # check if elements in smallHeap <= elements in largeHeap
        if self.small and self.large and (-1) * self.small[0] > self.large[0]:
            num = (-1) * heapq.heappop(self.small)
            heapq.heappush(self.large, num)
            
        # heap should be roughly same size
        if len(self.small) - len(self.large) >= 2:
            num = (-1) * heapq.heappop(self.small)
            heapq.heappush(self.large, num)    
        
        if len(self.large) - len(self.small) >= 2:
            num = (-1) * heapq.heappop(self.large)
            heapq.heappush(self.small, num)  
    
    # Time: O(1)
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return ((-1) * self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return (-1) * self.small[0]
        else:
            return self.large[0]
       
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

small-> []
large-> [6]
small-> [-6]
large-> [10]
small-> [-2]
large-> [6, 10]
small-> [-6, -2]
large-> [6, 10]
small-> [-5, -2]
large-> [6, 10, 6]
small-> [-5, -2, 0]
large-> [6, 10, 6]
small-> [-5, -2, 0]
large-> [6, 6, 6, 10]
small-> [-5, -3, 0, -2]
large-> [6, 6, 6, 10]
small-> [-3, -2, 0, -1]
large-> [5, 6, 6, 10, 6]
small-> [-3, -2, 0, -1, 0]
large-> [5, 6, 6, 10, 6]
small-> [-2, -1, 0, 0, 0]
large-> [3, 6, 5, 10, 6, 6]

       






