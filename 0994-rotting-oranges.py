from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        def get(x,y): 
            if 0<=x<height and 0<=y<width:
                return grid[x][y]
        frontier = set((x,y) for x in range(height) for y in range(width) if grid[x][y] == 2) # find all possible points
        print(frontier)
        deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        while frontier:
            print(frontier)
            frontier = set((x+dx,y+dy) for x,y in frontier for dx,dy in deltas if get(x+dx,y+dy) == 1)
            print(frontier)
            for x,y in frontier:
                grid[x][y] = 2
            count += 1
            print(count)
        if any(grid[x][y] == 1 for x in range(height) for y in range(width)):
            return -1
        elif count > 0:
            return count - 1
        else:
            return count
        
s=s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print()
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print()
print(s.orangesRotting([[[0,2]]]))



