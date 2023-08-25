
class Solution:
	# 135 / 138 testcases passed
	# The search is repeated for each valid increasing path.
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0
        
        def dfs(i, j, prev, l):
            nonlocal res
            res = max(res, l)
            if 0 <= i < m and 0 <= j < n and matrix[i][j] > prev:
                temp = matrix[i][j]
                matrix[i][j] = -1
                for dx, dy in dirs:
                    dfs(i+dx, j+dy, temp, l+1)
                matrix[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1, 0)
        return res

class Solution:
	# The search is repeated for each valid increasing path.
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0
        cache = {}

        def dfs(i, j):
            # return the longest increasing path starting from (i,j)
            nonlocal res
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = 1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    cache[(i,j)] = max(cache[(i,j)], 1+dfs(x,y))
            return cache[(i,j)]
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res



        


