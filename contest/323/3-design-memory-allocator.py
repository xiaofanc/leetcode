# memory allocator

class Allocator:

    def __init__(self, n: int):
        self.mem = [-1 for i in range(n)]
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        start = -1
        for i in range(self.n):
            if self.mem[i] == -1:
                cnt += 1
            else:
                cnt = 0
            if cnt >= size:
                start = i-size+1
                break
        if start == -1:
            return start
        else:
            for i in range(start, start+size):
                self.mem[i] = mID
        return start

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.mem[i] == mID:
                self.mem[i] = -1
                cnt += 1
        return cnt

        
class Allocator:

    def __init__(self, n: int):
        self.mem = [-1 for i in range(n)]
        self.n = n
        self.idToBlocks = collections.defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        start = -1
        for i in range(self.n):
            if self.mem[i] == -1:
                cnt += 1
            else:
                cnt = 0
            if cnt >= size:
                start = i-size+1
                break
        if start == -1:
            return start
        else:
            for i in range(start, start+size):
                self.mem[i] = mID
                self.idToBlocks[mID].append(i)
        return start

    def free(self, mID: int) -> int:
        if mID not in self.idToBlocks:
            return 0
        cnt = 0
        for b in self.idToBlocks[mID]:
            self.mem[b] = -1
            cnt += 1
        del self.idToBlocks[mID]
        return cnt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)