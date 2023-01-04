class MaxStack(list):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        if self.stack:
            m = max(x, self.stack[-1][1])
        else:
            m = x
        self.stack.append((x, m))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]

    def popMax(self): # O(n)?
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop())
        
        self.stack.pop()
        for x, m in reversed(b):
            self.push(x)
        return m

from sortedcontainers import SortedList
class MaxStack:
    # Two balanced tree
    # add, pop, remove for SortedList take O(logn) time
    def __init__(self):
        # sorted by id
        self.stack = SortedList()
        # sorted by value
        self.values = SortedList()
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.add((self.id, x))
        self.values.add((x, self.id))
        self.id += 1

    def pop(self) -> int:
        i, val = self.stack.pop()
        self.values.remove((val, i))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, i = self.values.pop()
        self.stack.remove((i, val))
        return val


class MaxStack:
    # maxheap + lazy update
    def __init__(self):
        self.stack = []
        self.heap = [] # maxheap
        self.removed = set() # store id removed for lazy update
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.append((self.id, x))
        heapq.heappush(self.heap, (-x, -self.id))
        self.id += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][0] in self.removed:
            self.stack.pop()
        i, val = self.stack.pop()
        self.removed.add(i)
        return val

    def top(self) -> int:
        while self.stack and self.stack[-1][0] in self.removed:
            self.stack.pop()
        return self.stack[-1][1]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]        

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        val, i = heapq.heappop(self.heap)
        self.removed.add(-i)
        return -val

