"""
LC 780
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.
The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).
 
Example 1:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

constraints: sx, sy, tx, ty > 1

approach:
if tx > ty: the previous coordinate must be (tx-ty, ty)
if tx < ty: the previous coordinate must be (tx, ty-tx)
"""

class Solution:
	# Time limit exceed
    def reachingPoints(self, sx, sy, tx, ty):
        if sx > tx or sy > ty:
            return False
        if sx == tx:
            # increase sy to ty by sx
            return (ty-sy) % sx == 0
        if sy == ty:
            return (tx-sx) % sy == 0
        
        if tx > ty:
            return self.reachingPoints(sx, sy, tx-ty, ty)
        elif ty > tx:
            return self.reachingPoints(sx, sy, tx, ty-tx)
        else:
            return False

    # Time O(log(max(tx, ty)))
    def reachingPoints(self, sx, sy, tx, ty):
        if sx > tx or sy > ty:
            return False
        if sx == tx:
            # increase sy to ty by sx
            return (ty-sy) % sx == 0
        if sy == ty:
            return (tx-sx) % sy == 0

        # when ty > sy and tx > sx
        if tx > ty:
        	# tx % ty < ty
            return self.reachingPoints(sx, sy, tx % ty, ty) 
        elif ty > tx:
            return self.reachingPoints(sx, sy, tx, ty % tx)
        else:
            return False

    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty-sy) % sx == 0
            if ty == sy:
                return (tx-sx) % sy == 0
            
            if tx > ty:
                tx = tx % ty
            elif tx < ty:
                ty = ty % tx
            else:
                return False
        return False

if __name__ == '__main__':
	s = Solution()
	print(s.reachingPoints(1, 1, 3, 5))  # True
	print(s.reachingPoints(1, 1, 2, 2))  # False

