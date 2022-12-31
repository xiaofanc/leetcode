class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # walks over every empty square exactly once
        m, n = len(grid), len(grid[0])
        x0, y0 = 0, 0
        nonobs = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    nonobs += 1
                if grid[i][j] == 1:
                    x0, y0 = i, j
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0
        def dfs(i, j):
            nonlocal res
            if len(visited) == nonobs and grid[i][j] == 2:
                res += 1
            for dx, dy in dirs:
                if i+dx < 0 or i+dx == m or j+dy < 0 or j+dy == n or (i+dx, j+dy) in visited or grid[i+dx][j+dy] == -1:
                    continue
                visited.add((i+dx, j+dy))
                dfs(i+dx, j+dy)
                visited.remove((i+dx, j+dy))
        
        visited = set()
        visited.add((x0, y0))
        dfs(x0, y0)
        return res

            