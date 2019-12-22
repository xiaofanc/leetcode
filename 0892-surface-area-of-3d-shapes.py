from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
            	# total surface area
                if grid[i][j]: res += grid[i][j] * 4 + 2      
                # i = 0, return False for if i
                if i: res -= min(grid[i][j], grid[i-1][j])*2  # neighbor
                if j: res -= min(grid[i][j], grid[i][j-1])*2  # neighbor
        return res

    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
                # total up and down surface area 
                if grid[i][j]: res += 2  
                # 4 neighbors around grid[i][j]
                for nr, nc in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= nr < n and 0 <= nc < n:
                        nval = grid[nr][nc]
                    else:
                        nval = 0
                    res += max((grid[i][j]-nval), 0)
        return res
        
if __name__ == '__main__':
	s = Solution()
	print(s.surfaceArea([[1,2],[3,4]]) == 34)