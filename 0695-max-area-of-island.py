class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        count = 0
        seen = set()
                
        def dfs(i, j):     
            if not (0 <= i < height and 0 <= j < width and (i,j) not in seen and grid[i][j] == 1):
                return 0
            
            seen.add((i,j))  
            return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1))
                
        for i in range(height):
            for j in range(width):
                count = max(dfs(i, j), count)
        return count

    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0

    def maxAreaOfIsland(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            # t: O(rc) s: O(1)
            max_area = 0
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] == 1:
                        max_area = max(max_area, self.explore(grid, r, c))
            return max_area

    def explore(self, grid, r, c):
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
            return 0
        if grid[r][c] == 0:
            return 0
        # mark as visited
        grid[r][c] = 0
        return 1 + self.explore(grid, r - 1, c) + self.explore(grid, r, c - 1) \
            + self.explore(grid, r + 1, c) + self.explore(grid, r, c + 1) 

    # stack
    def maxAreaOfIsland(self, grid):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    stack = []
    seen = set()
    ans = 0
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                area = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in directions:
                        if 0 <= (x+dx) < len(grid) and 0 <= (y+dy) < len(grid[0]) and grid[x+dx][y+dy] and (x+dx, y+dy) not in seen:
                            stack.append((x+dx, y+dy))
                            seen.add((x+dx, y+dy))
                ans = max(ans, area)
    return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 6




