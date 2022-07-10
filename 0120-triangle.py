from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for _ in range(len(triangle)-1):
            last = triangle.pop()
            triangle[-1] = [min(i,j) + k for i, j, k in zip(last[1:], last[0:-1], triangle[-1])]
        return triangle[0][0]

    # Time: O(n^2), there are n^2 cells in the triangle
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle)-1:
                path += min(min_path(row+1, col), min_path(row+1, col+1))
            return path
        
        return min_path(0, 0)

    # Time: O(n^2), there are n^2 cells in the triangle
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # in-place
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]) == -1)



    