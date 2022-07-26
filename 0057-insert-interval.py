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

    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < new[0]:
                res.append(interval)
            elif interval[0] > new[1]:
                res.append(new)
                res.extend(intervals[i:])
                return res
            else:
                new = [min(interval[0], new[0]), max(interval[1], new[1])]
        res.append(new)
        return res

    def add_interval(intervals, new_interval):
        result = []
        interval_to_merge = new_interval
        for i in range(len(intervals)):
            curr_interval = intervals[i]
            if curr_interval[1] < interval_to_merge[0]:
                result.append(curr_interval)
            elif interval_to_merge[1] < curr_interval[0]:
                result.append(interval_to_merge)
                interval_to_merge = curr_interval
            else:
                interval_to_merge = [min(curr_interval[0], interval_to_merge[0]), max(curr_interval[1], interval_to_merge[1])]
        result.append(interval_to_merge)
        return result
                  
if __name__ == '__main__':
	s = Solution()
	print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  #[[1,2],[3,10],[12,16]]
	print(s.insert([[1,5]], [2,3]))  # [1,5]

