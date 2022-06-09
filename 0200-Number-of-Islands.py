"""
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. During DFS, every visited node should be set as '0' to mark as visited node. Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.

  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

  # number of island = 3

linear scan the 2d matrix, if we find a node containing '1' then it is a root node. After we find the root node, we use DFS to turn the '1' around the root node into '0'. Continue the linear scan to find the next root node.

"""
from typing import List


class Solution:
    # DFS
    # Time: O(MxN), Space: O(MxN)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0: return 0
        height, width = len(grid), len(grid[0])
        deltas = [(0,-1), (0,1), (-1,0), (1,0)]
        n = 0

        # dfs makes the neighboring '1' to be '0' for the current island
        def dfs(x,y):
            if 0 <= x < height and 0 <= y < width and grid[x][y] == '1':
                grid[x][y] = '0'
                for dx, dy in deltas:
                    dfs(x+dx, y+dy)
                    
        for x in range(height):
            for y in range(width):
                if grid[x][y] == '1':
                    n += 1
                    dfs(x,y)
        return n

    # BFS
    # Space complexity : O(min(M, N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,N)
    def get_number_of_islands(M):
      rows, cols = len(M), len(M[0])
      res = 0
      dirs = [(1,0), (-1,0), (0,1), (0,-1)]
      
      def markIsland(i, j):
        queue = deque()
        queue.append((i, j))
        while queue:
          x, y = queue.popleft()
          M[x][y] = 0
          for dx, dy in dirs:
            newx, newy = x+dx, y+dy
            if 0 <= newx < rows and 0 <= newy < cols and M[newx][newy] == 1:
              queue.append((newx, newy))
      
      for i in range(rows):
        for j in range(cols):
          if M[i][j] == 1:
            res += 1
            markIsland(i, j)
      return res

if __name__ == '__main__':
    s = Solution()
    grid1 = [
        list('11110'),
        list('11010'),
        list('11000'),
        list('00000'),
    ]

    grid2 = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011'),
    ]

    print(s.numIslands(grid1))
    print(s.numIslands(grid2))