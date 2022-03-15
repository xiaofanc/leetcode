"""
LC 62.
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

create a new matrix with 0, and update the matrix with the paths at each point.
first row: only one path to each point, update all to 1
first col: only one path to each point, update all to 1
calculate the middle of matrix by adding the path from the left and the path from the up

[[0,0,0]
 [0,0,0]   -> 
 [0,0,0]]

[[1,1,1]
 [1,2,3]
 [1,3,6]]
"""

class Solution:
	# Time: O(n^2)
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1) 

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3) == 28)


