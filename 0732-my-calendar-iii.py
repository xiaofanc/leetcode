"""
1. sweep-line algorithm
2. segment tree
3. balanced tree
"""

from sortedcontainers import SortedDict
class MyCalendarThree:
    """
    sweep-line algorithm: use a differential array to represent the change that
    occurs at each time point.
    Time: log(N) to update the dict since it is sorted, O(N) to loop over the dict
    """

    def __init__(self):
        self.dct = SortedDict(int) # sort the key automatically

    def book(self, start: int, end: int) -> int:
        self.dct[start] = self.dct.get(start, 0) + 1
        self.dct[end] = self.dct.get(end, 0) - 1
        k = cur = 0
        for value in self.dct.values():
            cur += value
            k = max(k, cur)
        return k

if __name__ == '__main__':
	c = MyCalendarThree()
	print(c.book(10, 20))
	print(c.book(50, 60))
	print(c.book(10, 40))
	print(c.book(5, 15))



