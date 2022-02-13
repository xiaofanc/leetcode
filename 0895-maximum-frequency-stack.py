"""
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
"""

# too slow
class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = collections.defaultdict()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = self.count.get(val, 0) + 1

    def pop(self) -> int:
        maxcount = max(self.count.values())
        maxvals = [key for key, value in self.count.items() if value == maxcount]
        # print(self.count)
        # print("maxvals", maxvals)
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] in maxvals:
                val = self.stack[i]
                del self.stack[i]
                self.count[val] -= 1
                break
        return val
        

# Time: O(1)
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.count = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.count[f].append(val)

    def pop(self) -> int:
        # if 2 elements have the same freq, it will pop the recent one
        x = self.count[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.count[self.maxfreq]:
            self.maxfreq -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()