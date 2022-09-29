class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS
        dirs = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        m, n = len(grid), len(grid[0])
        if grid[0][0] or grid[m-1][n-1] != 0:
            return -1
        queue = deque()
        queue.append((0,0,1))
        visited = set()
        visited.add((0,0))
        while queue:
            x, y, path = queue.popleft()
            if x == m-1 and y == n-1:
                return path
            for dx, dy in dirs:
                if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
                    queue.append((x+dx, y+dy, path+1))
                    visited.add((x+dx, y+dy))
        return -1
        
if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])) # 4