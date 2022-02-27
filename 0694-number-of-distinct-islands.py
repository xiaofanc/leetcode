"""
num of unique path = number of distinct island
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, direction):
            if 0 <= i < m and 0<= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                dfs(i+1, j, "D")
                dfs(i-1, j, "U")
                dfs(i, j-1, "L")
                dfs(i, j+1, "R")
                path.append("0")
        
        unique_path = set()
        for i in range(m):
            for j in range(n):
                path = []
                if grid[i][j] == 1:
                    dfs(i, j, "0")
                if path:
                    unique_path.add(tuple(path)) # list cannot be added to set
        return len(unique_path)
                    

if __name__ == '__main__':
    s = Solution()
    print(s.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])) # 1