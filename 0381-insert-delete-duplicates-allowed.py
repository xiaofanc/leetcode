class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.v2i = defaultdict(list)
        self.size = 0

    def insert(self, val: int) -> bool:
        self.lst.append(val)
        if val in self.v2i:
            res = False
        else:
            res = True
        self.v2i[val].append(self.size)
        self.size += 1
        return res

    def remove(self, val: int) -> bool:
        if val not in self.v2i:
            return False
        # remove the last occurrence of val
        idx = self.v2i[val].pop()
        if len(self.v2i[val]) == 0:
            del self.v2i[val]
        # if not removing the last element, swap
        if idx != self.size-1:
            lastv = self.lst[-1]
            self.lst[-1], self.lst[idx] = val, lastv
            # update the index of the last element
            # update the largest index !
            # self.v2i[lastv] is not sorted after replacing the index !
            self.v2i[lastv].sort()
            self.v2i[lastv][-1] = idx
        # remove val
        self.lst.pop()
        self.size -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


