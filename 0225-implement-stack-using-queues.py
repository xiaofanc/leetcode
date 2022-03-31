
# use two Queue to implement Stack
from collections import deque
class MyStack:

    def __init__(self):
        # use queue_in to store elements and queue_out to pop
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            # add the elements of queue_in to queue_out except the last one
            self.queue_out.append(self.queue_in.popleft())
        # exchange in and out
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        # only one element left in queue_out
        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0

# use one Queue
class MyStack:

    def __init__(self):
        self.queue_in = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.queue_in)-1):
            self.queue_in.append(self.queue_in.popleft())
        return self.queue_in.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()