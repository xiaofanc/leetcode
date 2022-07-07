from typing import List

class Solution:
    # if there are multiple rotten oranges
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        def get(x,y): 
            if 0<=x<height and 0<=y<width:
                return grid[x][y]
        rotten = set((x,y) for x in range(height) for y in range(width) if grid[x][y] == 2) # find all possible points
        print(rotten)
        deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        while rotten:
            print(rotten)
            rotten = set((x+dx,y+dy) for x,y in rotten for dx,dy in deltas if get(x+dx,y+dy) == 1)
            print(rotten)
            for x,y in rotten:
                grid[x][y] = 2
            count += 1
            print(count)
        if any(grid[x][y] == 1 for x in range(height) for y in range(width)):
            return -1
        elif count > 0:
            return count - 1
        else:
            return count

    # if there are multiple rotten oranges
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        count = 0
        rotten = set((x,y) for x in range(m) for y in range(n) if grid[x][y] == 2)
        fresh = set((x,y) for x in range(m) for y in range(n) if grid[x][y] == 1)
        while fresh:
            if not rotten: return -1
            rotten = set((x+dx, y+dy) for (x,y) in rotten for dx, dy in directions if (x+dx, y+dy) in fresh)
            count += 1
            fresh -= rotten
        return count

    # use BFS to mark the rotten orange
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the rotten orange from the grid
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        # initialize a set to keep track of visited cell
        visited = set()
        fresh = 0
        # add the rotten orange to the deque, initialize min to 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        mins = 0
        # while queue is not empty
        while queue:
            # pop out the rotten orange from queue
            i, j, mins = queue.popleft()
            # mark neighbors as rotten is neighbor is a fresh orange
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited and grid[x][y] == 1:
                    queue.append((x, y, mins+1))
                    visited.add((x, y))
                    fresh -= 1
        # when the queue is empty, check if there are any fresh oranges left
        if fresh == 0:
            return mins
        return -1

s=s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print()
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print()
print(s.orangesRotting([[[0,2]]]))



