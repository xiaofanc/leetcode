
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            grid[i] = sorted(grid[i], reverse = True)
        
        res = 0
        for j in range(cols):
            maxv = float("-inf")
            for i in range(rows):
                maxv = max(grid[i][j], maxv)
            res += maxv
        return res
            
        