"""
LC 1381.
Implement the CustomStack class:
* CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
* void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
* int pop() Pops and returns the top of stack or -1 if the stack is empty.
* void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxn = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxn:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1
    
    # Time: O(n)
    def increment(self, k: int, val: int) -> None:
    	if not self.stack:
    		return
        for i in range(min(len(self.stack), k)):
            self.stack[i] = self.stack[i] + val

# O(1): 
# https://github.com/GuardianWang/LeetCode/tree/main/interview-exp



