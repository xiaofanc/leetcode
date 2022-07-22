import heapq
import math

# Time: O(n*logk). Space: O(k)
def closestKpoints(points, k):
    maxheap = []
    for point in points:
        dist = math.sqrt(point[0]**2 + point[1]**2)
        heapq.heappush(maxheap, (-dist, point))
        # print(maxheap)
        # pop out points which have larger distance if len(maxheap) > k
        if len(maxheap) > k:
            heapq.heappop(maxheap)
        # print("After ", maxheap)
    res = []
    for i in range(k):
      point = heapq.heappop(maxheap)[1]
      res.append(point)
    return res[::-1] # [[0, 0], [-2,2]]

print(closestKpoints([[1, 3], [-2, 2], [9, 9], [0, 0]], 2))
