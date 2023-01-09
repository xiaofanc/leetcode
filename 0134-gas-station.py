class Solution:
    # TLE: 33/37
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            j = 0
            tank = 0
            complete = True
            while j <= len(gas):
                # (i+j) % 5 is the station index
                curidx = (i+j) % len(gas)
                if tank + gas[curidx] < cost[curidx]:
                    complete = False
                    break
                else:
                    tank = tank - cost[curidx] + gas[curidx]
                    j += 1
            if complete:
                return i
        return -1

    def canCompleteCircuit(self, gas, cost):

        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        
        return starting_station if total_tank >= 0 else -1

