"""
Greedy:
If the heaviest person can share a boat with the lightest person, then do so. Otherwise, the heaviest person can't pair with anyone, so they get their own boat.
"""

class Solution:
    # [5,1,4,2], 6 -> 2
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # each boat carries at most two people
        l, r = 0, len(people)-1
        res = 0
        while l <= r:
            if l == r and people[l] <= limit:
                res += 1
                break
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # each boat carries at most two people
        l, r = 0, len(people)-1
        res = 0
        while l <= r:
            res += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            
        return res



        


    