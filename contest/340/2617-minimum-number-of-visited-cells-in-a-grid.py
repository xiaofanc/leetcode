# min step to move from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1)
# Starting from the cell (i, j), you can move to one of the following cells:
# Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
# Cells (k, j) with i < k <= grid[i][j] + i (downward movement).

# optimization:
# As reachable cells are continuous, we do not need to process these cells again:
	# g[i][k], where j < k <= grid[i][j] + j
	# g[k][j], where i < k <= grid[i][j] + i
# we skip ahead to the furthest k.

class Solution:
	# 1025 / 1055 test cases passed.
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [[float('inf') for j in range(n)] for i in range(m)]
        queue = deque()
        queue.append((0,0,1))
        while queue:
            i, j, step = queue.popleft()
            res[i][j] = min(res[i][j], step)
            # add possible next positions
            for k in range(i+1, min(grid[i][j] + i + 1, m)):
                queue.append((k, j, step+1))
            for k in range(j+1, min(grid[i][j] + j + 1, n)):
                queue.append((i, k, step+1))
        if res[-1][-1] != float('inf'):
            return res[-1][-1]
        return -1

class Solution:
	# BFS to get the minimum step
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # if a cell is visited, no need to check again
        visited = [[False for j in range(n)] for i in range(m)]
        queue = deque()
        queue.append((0,0))
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                # min step to reach the destination
                if i == m-1 and j == n-1:
                    return step
                # add possible next positions
                # optimization: add from the further cells first
                for k in range(min(grid[i][j] + i, m-1), i, -1):
                    if not visited[k][j]:
                        visited[k][j] = True
                        queue.append((k, j))
                for k in range(min(grid[i][j] + j, n-1), j, -1):
                    if not visited[i][k]:
                        visited[i][k] = True
                        queue.append((i, k))
            step += 1
        return -1
                
                
