from typing import List
import math
import heapq

class Solution:

    # time: O(nlogn+klogk), space: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = 0
        dists = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            heapq.heappush(dists, (dist, [x,y]))
            # print(dist, (x,y), dists)
        
        return [heapq.heappop(dists)[1] for i in range(k)]
    
    # time: O(nlogn)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0]**2 + p[1]**2)
        return points[:k]

    # time: O(n+nlogn), space: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = 0
        dists = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            dists.append([dist, (x,y)])
        dists.sort()
        # print(dist, dists)
        
        return [d[1] for d in dists[:k]]

    # time: O(nlogk), space: O(k)
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        maxHeap = []
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # result order does not matter
        return [value[1] for value in maxHeap]

if __name__ == '__main__':
    s = Solution()
    print(s.kClosest2([[1,3],[-2,2]], 1))
    print(s.kClosest2([[3,3],[5,-1],[-2,4]], 2))
    print(s.kClosest2([[100,99]], 3))


