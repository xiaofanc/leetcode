"""
DP:

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

build up a matrix finding the minimum path from top left to the bottom right 
grid[i][j].

cost(i,j)=grid[i][j]+min(cost(i-1,j),cost(i,j-1))

[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

[
 [1, 4, 5], 
 [2, 7, 6], 
 [6, 8, 7]
]


"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        cost = [[0]*width for _ in range(height)]
        cost[0][0] = grid[0][0]
        for x in range(1, height):
            cost[x][0] += grid[x][0] + cost[x-1][0]
        for y in range(1, width):
            cost[0][y] += grid[0][y] + cost[0][y-1]
        for x in range(1, height):
            for y in range(1, width):
                cost[x][y] = grid[x][y] + min(cost[x-1][y], cost[x][y-1])
        #for c in cost: print(c)
        return cost[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[-1][-1]
            
    #inplace        
    def minPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        for x in range(1, height):
            grid[x][0] += grid[x-1][0] 
        for y in range(1, width):
            grid[0][y] += grid[0][y-1]
        for x in range(1, height):
            for y in range(1, width):
                grid[x][y] += min(grid[x-1][y], grid[x][y-1])
        #for c in grid: print(c)
        return grid[-1][-1]
                
if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7)


