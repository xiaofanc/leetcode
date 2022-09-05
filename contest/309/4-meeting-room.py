"""
2402.
"""
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # res to store meetings for each room
        res = [0]*n
        # heap to store meeting rooms (endtime, room#)
        h = []
        meetings.sort()
        for i in range(n): # each room end with 0 in the beginning
            heapq.heappush(h, (0, i))

        for i, meeting in enumerate(meetings):
            end, room = heapq.heappop(h)
            # meeting will take place in the unused room with the lowest number
            if meeting[0] >= end:
                # print("heap-->", h)
                select = room
                temp = [(end, room)]
                # print("h->", h)
                while h and h[0][0] <= meeting[0]:
                    nextEnd, nextRoom = heapq.heappop(h)
                    if nextRoom < select:
                        select = nextRoom
                    temp.append((nextEnd, nextRoom))
                for end, room in temp:
                    if room != select:
                        heapq.heappush(h, (end, room))
                    else:
                        heapq.heappush(h, (meeting[1], room))
                res[select] += 1
            # wait for the first room that ends
            else: 
                res[room] += 1
                newEnd = end+(meeting[1]-meeting[0])
                heapq.heappush(h, (newEnd, room))
        # print("res", res)
        return res.index(max(res))
        
if __name__ == '__main__':
    s = Solution()
    print(s.mostBooked(4, [[19,20],[14,15],[13,14],[11,20]])) # 1 -> [13,14],[14,15]
    print(s.mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]]))  # 0 
    print(s.mostBooked(1, [[0,1]]))  # 0 





        