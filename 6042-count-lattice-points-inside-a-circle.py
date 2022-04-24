"""
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:
A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.

"""
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for circle in circles:
            x0, y0, r = circle[0], circle[1], circle[2]
            for x in range(x0-r, x0+r+1):
                for y in range(y0-r, y0+r+1):
                    if (x,y) in res: 
                        continue
                    if (x-x0)**2 + (y-y0)**2 <= r**2:
                        res.add((x,y))
        return len(res)

if __name__ == '__main__':
	s = Solution()
	print(s.countLatticePoints([[2,2,2],[3,4,1]]))  #16