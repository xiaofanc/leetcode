"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
"""
from typing import List

class Solution:
    def canAttendMeetings0(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if self.overlap(intervals[i], intervals[j]):
                    return False
        return True
    
    def overlap(self, intervals1, intervals2):
        #return intervals[i][0] <= intervals[j][0] < intervals[i][1] or intervals[j][0] <= intervals[i][0] < intervals[j][1]
        return min(intervals1[1], intervals2[1]) > max(intervals1[0], intervals2[0])
    
    def canAttendMeetings1(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        if len(intervals) == 1:
            return True
        intervals = sorted(intervals)
        #print(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings0([[0,30],[15,20],[5,10]])) # False
    print(s.canAttendMeetings1([[0,15],[15,20],[5,10]])) # False
    print(s.canAttendMeetings1([[0,30]])) # True

    