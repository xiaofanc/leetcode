class Solution:
    # TLE: 116 / 198 test cases passed.
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        minStop = len(stations)+1
        
        def backtrack(i, fuel, position, comb):
            nonlocal minStop
            if len(comb) > minStop:
                return
            if fuel-(target-position) >= 0:
                minStop = min(minStop,len(comb))
                return
            for j in range(i, len(stations)):
                station, addFuel = stations[j][0], stations[j][1]
                if fuel - (station-position) >= 0:
                    comb.append(stations[j])
                    backtrack(j+1, fuel - (station-position) + addFuel, station, comb)
                    comb.pop()
        backtrack(0, startFuel, 0, [])
        return -1 if minStop == len(stations)+1 else minStop
    
    # DP: O(N^2)           
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp = [i] the farthest location we can get to using i refueling stops
        dp = [startFuel] + [0] * len(stations)
        for i, (loc, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                # if using t stops, it can reach the location
                # then car can fuel at this station
                if dp[t] >= loc: 
                    dp[t+1] = max(dp[t+1], dp[t]+capacity)
                    print("dp", dp)
        
        for i, pos in enumerate(dp):
            if pos >= target:
                return i
        return -1

    # heap: O(NlogN)
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        pq = [] # max heap to store capacity of each gas station we've driven by
        # When we reach a station but have negative fuel, we need to find the largest gas stations we've driven by until the fuel is non-negative
        ans = prev = 0
        stations.append((target, 0))
        for location, capacity in stations:
            tank -= location - prev
            while tank < 0 and pq:
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: # not enough fuel from previous stations
                return -1
            heapq.heappush(pq, -capacity)
            prev = location
            
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minRefuelStops(1, 1, [])) # 0
    print(s.minRefuelStops(100, 1, [[10,100]])) # -1
    print(s.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]])) # 2




