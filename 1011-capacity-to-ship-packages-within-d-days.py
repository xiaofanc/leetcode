

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min cap: max(weights), max cap: sum(weights)
        # binary search
        def canfinish(cap, weights, days):
            done = [False] * len(weights)
            for i in range(len(weights)):
                # start a new day
                if not done[i]: 
                    maxcap = cap
                    days -= 1
                    # max packages loaded at that day
                    while i < len(weights) and maxcap - weights[i] >= 0:
                        maxcap -= weights[i]
                        done[i] = True
                        i += 1
            return days >= 0

        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r-l)//2
            if canfinish(m, weights, days):
                r = m
            else:
                l = m+1
        return l
