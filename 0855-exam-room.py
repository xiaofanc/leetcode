class ExamRoom:
    # TLE, 1 did not pass
    def __init__(self, n: int):
        # self.L to record people
        self.n, self.L = n, []

    def seat(self) -> int:
        # calculate the distances for each line, find the longest
        # distance between 0 and first person
        if not self.L:
            pos = 0
        else:
            d = self.L[0] 
            # d = distance at the start
            pos = 0
            # d = distance in the middle
            # closest person => so (b-a)//2
            for a, b in zip(self.L, self.L[1:]):
                if (b-a)//2 > d:
                    d = (b-a)//2
                    pos = (a+b)//2
            # d = distance in the end
            if self.n-1-self.L[-1] > d:
                pos = self.n-1
        bisect.insort(self.L, pos)
        return pos

    def leave(self, p: int) -> None:
        self.L.remove(p)
        

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        # initialize heap
        self.pq = [(self.dist(-1, n), -1, n)]  
    
    def dist(self, x, y):
        # self.pq is maxheap
        if x == -1:
            return -y
        elif y == self.n:
            return -(self.n-1-x)
        else:
            return -(abs(y-x)//2)

    # O(nlogn)
    def seat(self) -> int:
        # pop the longest line
        d, x, y = heapq.heappop(self.pq)
        # if the line has a fake head or tail
        if x == -1:
            pos = 0
        elif y == self.n:
            pos = self.n-1
        else:    
            pos = (x+y)//2
        heapq.heappush(self.pq, (self.dist(x, pos), x, pos))
        heapq.heappush(self.pq, (self.dist(pos, y), pos, y))
        return pos

    # O(n) - heapify
    def leave(self, p: int) -> None:
        # find the head and tail
        x = y = None
        for interval in self.pq:
            if interval[1] == p:
                y = interval
            if interval[2] == p:
                x = interval
            if x and y:
                break
        # combine x and y
        self.pq.remove(x)
        self.pq.remove(y)
        self.pq.append((self.dist(x[1], y[2]), x[1], y[2]))
        # important! re-heapify after deletion, takes O(n)
        heapq.heapify(self.pq) 



