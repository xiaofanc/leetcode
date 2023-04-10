class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            for dx, dy in dirs:
                if 0 <= i+dx < rows and 0 <= j+dy < cols and grid[i+dx][j+dy] == 1:
                    dfs(i+dx, j+dy)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 1:
                    dfs(i, j)
        
        print(grid)
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += 1
        return res




        