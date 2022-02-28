"""
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

"""
class MyCircularQueue:
    # Time: O(1), Space: O(n)
    def __init__(self, k: int):
        "list end can be found by headindex+count-1"
        self.list = [0] * k
        self.headindex = 0
        self.n = k
        self.count = 0
        
    def enQueue(self, value: int) -> bool:
        if self.count == self.n:
            return False
        self.list[(self.headindex + self.count) % self.n] = value
        self.count += 1
        # print("self.list", self.list)
        return True
        
    def deQueue(self) -> bool:
        "list does not change, only move the headindex"
        if self.count == 0:
            return False
        self.headindex = (self.headindex + 1) % self.n
        self.count -= 1
        # print("deque -> self.list", self.list)
        return True
    
    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.list[self.headindex]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.list[(self.headindex + self.count -1) % self.n]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()




