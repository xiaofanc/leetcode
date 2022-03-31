class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        
    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        return self.stack_in[0]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2 


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2, param_3, param_4)