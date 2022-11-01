class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        res = []
        
        def dfs(i, j):
            if i == rows:
                res.append(j)
                return 
            if grid[i][j] == 1: 
                # if hit the wall or V-shape
                if j == cols-1 or grid[i][j+1] == -1:
                    res.append(-1)
                    return
                else:
                    dfs(i+1, j+1)
            else:
                # if hit the wall or V-shape
                if j == 0 or grid[i][j-1] == 1:
                    res.append(-1)
                    return
                else:
                    dfs(i+1, j-1)
        
        for j in range(cols):
            dfs(0, j)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))




    