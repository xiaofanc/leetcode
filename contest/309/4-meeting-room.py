class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap to store meeting rooms (endtime, room#)
        res = [0]*n
        h = []
        meetings.sort()
        if len(meetings) <= n:
            return 1
        for i, meeting in enumerate(meetings[:n]):
            heapq.heappush(h, (meeting[1], i))
        print("heap->", h)
        for i, meeting in enumerate(meetings[n:]):
            end, room = heapq.heappop(h)
            res[room] += 1
            if meeting[0] < end:  # no unused room
                newEnd = end+(meeting[1]-meeting[0])
                heapq.heappush(h, (newEnd, room))
            else:
                # need to find the unused room with the lowest number
                select = room
                temp = [(end, room)]
                while h[0][0] >= meetings[0]:
                    nextEnd, nextRoom = heapq.heappop(h)
                    if nextRoom < select:
                        select = nextRoom
                    temp.append((nextEnd, nextRoom))
                for end, room in temp:
                    if room != select:
                        heapq.heappush(h, (end, room))
                    else:
                        heapq.heappush(h, (meeting[1], room))
        return max(res)
        
            
        
        