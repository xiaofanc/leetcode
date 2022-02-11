"""
u need to combine the numbers if they are in range. eg: 1, 3 - they cannot be combined as there is num missing to form a range So we need to output it as separate ranges [1,1] and [3,3] . Inorder to have range [1,3] u need 2. only if u hv 2 can u combine it in one range saying [1, 3] (1,2,3)

empty + 1 = [1,1]
[1,1] , [4,4] + 6 = [1,1], [4,4] , [6,6]
[1,1] , [3,3] + 2 = [1,3]
[1,1] , [4,4] + 5 = [1,1] , [4,5]
[1,1] , [4,4] + 3 = [1,1] , [3,4]
[1,2,3] + [5,6,7] + 4 = [1,2,3,4,5,6,7]

"""

class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set() # heap cannot have the same key

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])
        
    def getIntervals(self) -> List[List[int]]:
        # merge intervals
        temp = []
        while self.intervals:
            cur = heapq.heappop(self.intervals)
            if temp and temp[-1][1] + 1 >= cur[0]: # [1,5] + [6,6] => merge
                # merge
                temp[-1][1] = cur[1]
            else:
                temp.append(cur)
        
        self.intervals = temp
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
