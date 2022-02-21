from typing import List

class Solution:
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

s=s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print()
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print()
print(s.orangesRotting([[[0,2]]]))



