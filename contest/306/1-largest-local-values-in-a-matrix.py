"""
2373.
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
"""

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n-3+1
        maxLocal = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                maxM = 0
                x, y = i+1, j+1
                for a in range(x-1, x+2):
                    for b in range(y-1, y+2):
                        maxM = max(maxM, grid[a][b])
                maxLocal[i][j] = maxM
        return maxLocal
