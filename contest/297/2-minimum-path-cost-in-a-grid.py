"""
You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from cells in the last row.

Each possible move has a cost given by a 0-indexed 2D array moveCost of size (m * n) x n, where moveCost[i][j] is the cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last row of grid can be ignored.

The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.
"""

class Solution:
    # TLE
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = float("inf")

        def calCost(comb):
            cost = 0
            for i in range(1, len(comb)):
                v1, r1, c1 = comb[i-1]
                v2, r2, c2 = comb[i]
                cost += v1
                cost += moveCost[v1][c2]
            cost += comb[len(comb)-1][0]
            return cost
            
        def combinations(i, comb):
            nonlocal res
            if comb != [] and calCost(comb) > res:
                return
            if len(comb) == m:
                # print("comb", comb)
                res = min(res, calCost(comb))
                return
            for j in range(n):
                comb.append((grid[i][j], i, j))
                combinations(i+1, comb)
                comb.pop()
                
        combinations(0, [])
        return res

        # DP
        def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
            cost = [grid[0][:]]
            for r, row in enumerate(grid):
                if r > 0:
                    # get a new row
                    cost.append([])
                    # calculate mincost for each position in the row
                    # mincost = cell+min(pathsum)
                    for c, cell in enumerate(row):
                        cost[-1].append(cell+min(cost[-2][i] + moveCost[val][c] for i, val in enumerate(grid[r-1])))
            # get the mincost for the last row
            return min(cost[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])) # cost [[5, 3], [23, 8], [19, 17]], res = 17





            