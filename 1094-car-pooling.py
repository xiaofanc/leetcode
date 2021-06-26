class Solution:

    # time: O(nlogn), space: O(n)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_dct = {}
        for trip in trips:
            # key: bus stop, value: change of passengers
            passengers, start, end = trip[0], trip[1], trip[2]
            if start in trip_dct:
                trip_dct[start] += passengers
            else:
                trip_dct[start] = passengers
            if end in trip_dct:
                trip_dct[end] -= passengers
            else:
                trip_dct[end] = -passengers
        
        # sort the stops map
        stops = {k: v for k, v in sorted(trip_dct.items(), key=lambda item: item[0])}
        # print(stops)
        
        # calculate the total passengers in the bus for each stop
        total_passengers = 0
        for k, v in stops.items():
            # print(k, v)
            total_passengers += v
            if total_passengers > capacity:
                return False
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_dct = {}
        for trip in trips:
            # key: bus stop, value: change of passengers
            passengers, start, end = trip[0], trip[1], trip[2]
            if start in trip_dct:
                trip_dct[start] += passengers
            else:
                trip_dct[start] = passengers
            if end in trip_dct:
                trip_dct[end] -= passengers
            else:
                trip_dct[end] = -passengers
            
        # calculate the total passengers in the bus for each stop
        total_passengers = 0
        for k in sorted(trip_dct.keys()):
            # print(k, v)
            total_passengers += trip_dct[k]
            if total_passengers > capacity:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.carPooling([[2,1,5],[3,5,7]], 3)) # true
    print(s.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11)) # true
    print(s.carPooling([[2,1,5],[3,3,7]], 4)) # false
