"""
Explanation:
Sort cars by the start positions pos
Loop on each car from the end to the beginning
Calculate its time needed to arrive the target
cur records the current biggest time (the slowest)

If another car needs less or equal time than cur,
it can catch up this car fleet.

If another car needs more time,
it will be the new slowest car,
and becomes the new lead of a car fleet.
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of the slowest car from the end to beginning
        # do not start from beginning since we cannot make sure whether the car forward will drive at the same speed
        time = []
        cur = res = 0
        for p, s in sorted(zip(position, speed)):
            time.append((target-p)/s)
        
        for t in time[::-1]:
            if t > cur:  # cannot catch the car forward
                res += 1
                cur = t
        return res

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # keep track of the slowest car using non-decreasing stack
        stack = []
        for p, s in sorted(zip(position, speed))[::-1]: # reversed sorted order
            newT = (target-p)/s
            if not stack:
                stack.append(newT)
            else:
                # if new slowest car, append
                if newT > stack[-1]: 
                    stack.append(newT)
                # else faster than the forward car, merge to one car fleet
        return len(stack)  

if __name__ == '__main__':
	s = Solution()
	print(s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3 


