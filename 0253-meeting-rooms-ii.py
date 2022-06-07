"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
minheap to keep track of the meeting end time for each room.
"""
class Solution:
    # time: O(nlogn), space: O(n)
    def minMeetingRooms(self , intervals: List[List[int]]) -> int:
        intervals.sort()
        if not intervals:
            return 0
        free_rooms = []
        
        # push the first meeting end time, we have to give a new room to the first meeting
        heapq.heappush(free_rooms, intervals[0][1]) 
        
        for i in intervals[1:]:
            # compare with the minimum end time of the each room
            # if the current meeting start time is >= the minimum end time of the rooms
            # reuse that room which ends early
            if i[0] >= free_rooms[0]:
                # no need to add a new room, update the end time of the room which will be used
                # pop the smallest value and push the new item
                heapq.heapreplace(free_rooms, i[1])
                # print(free_rooms)
            # else add a new room
            else:
                heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)

    # time: O(nlogn), space: O(n)
    def minMeetingRooms(self , intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        
        s, e = 0, 0 
        rooms = 0
        # The start pointer simply iterates over all the meetings
        # The end pointer helps us track if a meeting has ended and if we can reuse a room
        while s < len(start_times):
            if start_times[s] < end_times[e]:
                rooms += 1
                s += 1
            else: # a room is empty
                s += 1
                e += 1
        return rooms
                

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        # arrage meeting rooms based on the start time
        # need to know when the meeting ends first
        minheap = []
        heapq.heappush(minheap, intervals[0][1])
        for interval in intervals[1:]:
            # if next meeting start time is later than the smallest end time, then pop the min and update the end time
            if minheap[0] <= interval[0]:
                heapq.heappop(minheap)
            # else need to add a new room
            heapq.heappush(minheap, interval[1])
        return len(minheap)

if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms([[1,5],[8,9],[8,9]])) #2
    print(s.minMeetingRooms([[0,30],[5,10],[15,20]])) #2

