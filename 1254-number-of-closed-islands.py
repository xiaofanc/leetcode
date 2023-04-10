"""
land in the border is not surrounded by water

"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                for dx, dy in directions:
                    dfs(i+dx, j+dy)
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 0:
                    dfs(i, j)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(x, y):
            if x in (0, m-1) or y in (0, n-1):
                self.isIsland = False 
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = -1 
                    dfs(i, j)
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.isIsland = True
                    dfs(i, j)
                    res += self.isIsland
                    
        return res 
                            
if __name__ == '__main__':
    s = Solution()
    grid = [[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]]

    print(s.numIslands(grid)) # 2
