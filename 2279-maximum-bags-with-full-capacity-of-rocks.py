class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        
        capacity.sort()
        res = 0
        for i in range(len(capacity)):
            additionalRocks -= capacity[i]
            if additionalRocks >= 0:
                res += 1
            else:
                break 
        return res