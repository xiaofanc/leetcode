

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval[1])
            else:
                top = heap[0]
                if interval[0] <= top:
                    heapq.heappush(heap, interval[1]) # new room
                else:
                    heapq.heappop(heap) # an available room
                    heapq.heappush(heap, interval[1]) # new end time for that room
        return len(heap)
                    
            