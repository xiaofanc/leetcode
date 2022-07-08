"""
num of unique path = number of distinct island
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        deltas = [(0,-1,'L'), (0,1,'R'), (-1,0,'U'), (1,0,'D')]

        def dfs(i, j, direction):
            if 0 <= i < m and 0<= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(direction)
                for dx, dy, d in deltas:
                    dfs(x+dx, y+dy, d)
                path.append("0")  # mark return is needed! ["0RRR0U", "0RR0RU"]
        
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