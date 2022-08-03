"""
min stack:
store min value in the stack at the same time

warning:
do not use self.minval in the initialization:
self.minval will change due to poping, therefore using the minval from the top
of the stack !

push, push, push, pop, push, getMin
-10, 14, -20, [], -7, ?
[(-10,-10),(14,-10),(-20,-20)]
[(-10,-10),(14,-10),(-7,-10)]  (-7 should use -10 from previous, rather than -20 from self.minval)
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append((x, min(self.getMin(),x)))

    def pop(self):
        return self.stack.pop()
        
    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())     
    print(minStack.getMin())  