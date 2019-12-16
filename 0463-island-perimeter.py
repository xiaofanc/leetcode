from typing import List

class Solution:
    #looking 0 around
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
        height, width = len(grid), len(grid[0])
        def get_grid(x, y):
            if 0 <= x < height and 0 <= y < width:
                return grid[x][y]
            else:
                return 0
        ans = 0   
        for x in range(height):
            for y in range(width):
                if grid[x][y] == 1:
                    ans += sum(get_grid(x+dx, y+dy) == 0 for dx, dy in neighbors)
        return ans
    
    # looking 1
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    ans += 4
                    # check the cell below
                    if i < height - 1 and grid[i+1][j] == 1:
                        ans -= 2
                    # check the cell right
                    if j < width - 1 and grid[i][j+1] == 1:
                        ans -= 2  # cells have one side next to each other
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16)