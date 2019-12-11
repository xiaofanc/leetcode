    def lastStoneWeight(self, A):
        pq = [-x for x in A]
        heapq.heapify(pq)
        for i in xrange(len(A) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]