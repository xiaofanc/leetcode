
from collections import deque

# BFS find the shortest path
def shortestCellPath(grid, sr, sc, tr, tc):	
  rows, cols = len(grid), len(grid[0])
  queue = deque([([sr, sc], 0)])
  dirs = [(1,0),(-1,0),(0,1),(0,-1)]
  visited = set((sr, sc))
  while queue:
    point, depth = queue.popleft()
    if point[0] == tr and point[1] == tc:
      return depth
    for dx, dy in dirs:
      newx, newy = point[0]+dx, point[1]+dy
      if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 1 and (newx, newy) not in visited:
        visited.add((newx, newy))
        queue.append(([newx, newy], depth+1))
        # print("queue", queue)
  return -1
        

print(shortestCellPath([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]], 0,0,2,0)) # 8
print(shortestCellPath([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]], 0,0,2,0)) # 2