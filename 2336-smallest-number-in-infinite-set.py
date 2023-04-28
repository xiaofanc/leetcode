class SmallestInfiniteSet:

    def __init__(self):
        self.poped = set()

    def popSmallest(self) -> int:
        for i in range(1, 1001):
            if i not in self.poped:
                self.poped.add(i)
                return i

    def addBack(self, num: int) -> None:
        if num in self.poped:
            self.poped.remove(num)
            

class SmallestInfiniteSet:

    def __init__(self):
        self.addedback = []    # store numbers before present
        self.addedset = set(). # store numbers before present
        self.present = 1

    def popSmallest(self) -> int:
        if self.addedback:
            n = heapq.heappop(self.addedback)
            self.addedset.remove(n)
            return n
        else:
            self.present += 1
            return self.present-1

    def addBack(self, num: int) -> None:
        # if num is already existed
        if num in self.addedset or num >= self.present:
            return
        self.addedset.add(num)
        heapq.heappush(self.addedback, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

