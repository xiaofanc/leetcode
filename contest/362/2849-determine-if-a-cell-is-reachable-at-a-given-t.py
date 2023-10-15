"""
Approach:
- Find the min time taken to reach the destination & if it is less than t then return true.
- Only edge case is when the source and destination both are equal and t = 1, in this case its not possible to reach destination in t time.

How to find min distance ?
- find the diff of x and y
- we can take min(diffx, diffy) steps in the diagonal direction
- then take abs(diffx-diffy) steps in the horizontal or vertical direction
- if it is less than t then return True

edge case:
- start == end and t = 1, return False
"""

class Solution:
	#[1,1,1,1,2] -> True
	#[1,1,1,1,1] -> True
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False
        diffx, diffy = abs(fx-sx), abs(fy-sy)
        return min(diffx, diffy) + abs(diffy-diffx) <= t

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # min step to reach the destination
        need = max(abs(sx - fx), abs(sy - fy))
        return t >= need if need else t != 1
                

