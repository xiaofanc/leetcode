class Solution:

    def __init__(self, w: List[int]):
        self.lst = w

    def pickIndex(self) -> int:
        # return index of the value picked
        # random.choices() return a list
        return random.choices([_ for _ in range(len(self.lst))], weights = self.lst)[0]


# rephrase do sampling with weight: given a list of offsets (i.e. prefix sums) and a target offset, our task is to fit the target offset into the list so that the ascending order is maintained.
# inserting an element into a sorted list.
class Solution:
    def __init__(self, w: List[int]):
        # prefix sum
        self.s = [w[0]]
        for n in w[1:]:
            self.s.append(self.s[-1]+n)

    def pickIndex(self) -> int:
        # generate a value from [0,1], scale up
        target = self.s[-1] * random.random()
        # find the right position to insert
        for i, s in enumerate(self.s):
            if s >= target:
                return i
        
        # i = bisect.bisect_left(self.s, target)
        # return i


        