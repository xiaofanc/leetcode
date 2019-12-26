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