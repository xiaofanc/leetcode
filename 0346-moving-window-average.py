from collections import deque
class MovingAverage0:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        sum_ = sum(queue[-size:])
        
        return sum_ / min(len(queue), size)


class MovingAverage1:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.size, self.count)

if __name__ == '__main__':
    m = MovingAverage0(3)
    print(m.next(1)) #1
    print(m.next(10)) #(1 + 10) / 2
    print(m.next(3)) #(1 + 10 + 3) / 3
    print(m.next(5)) #(10 + 3 + 5) / 3
    n = MovingAverage1(3)
    print(n.next(1)) #1
    print(n.next(10)) #(1 + 10) / 2
    print(n.next(3)) #(1 + 10 + 3) / 3
    print(n.next(5)) #(10 + 3 + 5) / 3
