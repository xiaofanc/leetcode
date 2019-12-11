from typing import List
import heapq
#from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-p for p in stones]
        heapq.heapify(pq)
        for i in range(len(stones)-1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x-y))
        return -pq[0]
        
if __name__ == '__main__':
	s = Solution()
	print(s.lastStoneWeight([2,7,4,1,8,1]) == 1)