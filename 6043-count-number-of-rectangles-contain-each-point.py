"""
You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).
The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
Output: [2,1]
Explanation: 
The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].
"""


class Solution:
	# Time limit exceeds
    def countRectangles(self, rectangles, points):
        ans = []
        rectangles = sorted(rectangles, key = lambda x: x[0], reverse = True)
        for point in points:
            res = 0
            x, y = point[0], point[1]
            for i, rec in enumerate(rectangles):
                l, h = rec[0], rec[1]       
                if x > l:
                    break
                if y > h:
                    continue
                else:
                    res += 1
            ans.append(res)
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.countRectangles([[1,1],[2,2],[3,3]], [[1,3],[1,1]])) # [1,3]
	print(s.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]])) # [2,1]






