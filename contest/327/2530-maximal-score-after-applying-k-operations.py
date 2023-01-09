class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for n in nums:
            heapq.heappush(heap, -n)
        
        for i in range(k): # O(klogn)
            maxn = -heapq.heappop(heap)
            res += maxn
            heapq.heappush(heap, -math.ceil(maxn/3))
        return res
            