"""
You are given an array of non-overlapping intervals intervals, insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        # next interval to be added
        start, end = new 
        for istart, iend in intervals:
            if start > iend:
                res.append([istart, iend])
            elif istart > end:
                res.append([start, end])
                start, end = istart, iend
            elif iend >= start or istart <= end:
                start = min(start, istart)
                end = max(end, iend)
        # finally
        res.append([start, end])
        return res
      
if __name__ == '__main__':
	s = Solution()
	print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]

