"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) < 2:
            return 0

        # sort by the end of the intervals
        # since we prefer to keep the non-overlapping intervals with the small end
        intervals_sorted = sorted(intervals, key = lambda x: x[1])
        # interval.sort(key = lambda x: x[1])
        # stack to store maximum nonoverlapping intervals
        stack = [intervals_sorted[0]]
        
        for i in range(1, len(intervals_sorted)):
            if intervals_sorted[i][0] >= stack[-1][1]: # not overlap
                stack.append(intervals_sorted[i])
        
        return len(intervals)-len(stack)

                
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        
        intervals.sort(key = lambda x: x[1])
        total = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                total += 1
            else:
                prev = intervals[i][1]
        return total

if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))  # 2
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1







