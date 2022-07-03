"""
Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
"""

class Solution:
    # DFS - TLE
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        paths = 0
        visited = set()
        
        def dfs(i, j, prev):
            nonlocal paths
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] <= prev or (i, j) in visited:
                return
            paths += 1
            visited.add((i, j))
            for dx, dy in dirs:
                dfs(i+dx, j+dy, grid[i][j])
            visited.remove((i, j))
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0)
        return paths % (10**9 + 7)

    # DFS + memo
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        paths = 0
        visited = {}
        
        def dfs(i, j, prev):
            if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] <= prev:
                return 0
            if (i, j) in visited:
                return visited[(i, j)]
            ans = 1
            for dx, dy in dirs:
                ans += dfs(i+dx, j+dy, grid[i][j])
            visited[(i, j)] = ans
            return ans
        
        for i in range(rows):
            for j in range(cols):
                paths += dfs(i, j, 0)
        return paths % (10**9 + 7)





        
            