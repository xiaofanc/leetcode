import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        if not piles:
            return 0
        h = []
        for p in piles:
            heapq.heappush(h, -p)
        for i in range(k):
            if h:
                maxp = -heapq.heappop(h)
                maxp -= maxp // 2
                if maxp > 0:
                    heapq.heappush(h, -maxp)
        return -sum(h)
