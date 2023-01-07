class Solution:
    # does not always work when selcting max i+j
    def removeOnes(self, grid: List[List[int]]) -> int:
        # rows: [3, 3, 1]
        # cols: [2, 3, 2] 
        # [1, 1]
        # rows: [2, 0, 0]
        # cols: [1, 0, 1] 
        # [0, 0]
        # rows: [0, 0, 0]
        # cols: [0, 0, 0] 

        m, n = len(grid), len(grid[0])
        rows, cols = [0]*m, [0]*n
        candidates = set()
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
                if grid[i][j] == 1:
                    candidates.add((i, j))
        res = 0
        while True:
            if len(candidates) == 0:
                return res
            maxn, n1, n2 = 0, 0, 0
            for pair in candidates:
                i, j = pair[0], pair[1]
                if rows[i] + cols[j] > maxn:
                    maxn = rows[i] + cols[j]
                    n1, n2 = i, j
            # remove 1 in rows n1 and col n2
            # update rows, cols and grid, candidates
            print("n1, n2", n1, n2)
            for i in range(m):
                if grid[i][n2] == 1:
                    grid[i][n2] = 0
                    candidates.remove((i, n2))
                    rows[i] -= 1
                    cols[n2] -= 1
            for j in range(n):
                if grid[n1][j] == 1:
                    grid[n1][j] = 0
                    candidates.remove((n1, j))
                    rows[n1] -= 1
                    cols[j] -= 1
            print("rows, cols", rows, cols)
            res += 1
                    
class Solution:
    # check the min operation to visit all rows and cols with one
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        res = float('inf')

        def backtrack(cnt):
            nonlocal res
            flag = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and ('r',i) not in seen and ('c', j) not in seen:
                        flag = True
                        seen.add(('r', i))
                        seen.add(('c', j))
                        backtrack(cnt+1)
                        seen.remove(('r', i))
                        seen.remove(('c', j))
            if flag == False: # end
                res = min(res, cnt)
        backtrack(0)
        return res

                    
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def count_ones(grid):
            return sum([grid[r].count(1) for r in range(ROWS)])
        
        def move_to_zero(r, c):
            for i in range(COLS): grid[r][i] = 0
            for i in range(ROWS): grid[i][c] = 0
            
        def restore_from_copy(copy, r, c):
            for i in range(COLS): grid[r][i] = copy[r][i]
            for i in range(ROWS): grid[i][c] = copy[i][c]
                
        def copy():                
            return [grid[r][:] for r in range(ROWS)]
        
        def backtracking():
            ones_count = count_ones(grid) # recount every time
            if ones_count == 0:
                return 0

            result = math.inf
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 1:
                        # make a copy of the current grid
                        grid_copy = copy() 

                        # update the current grid
                        move_to_zero(row, col) 

                        # move to next one
                        candidate_value = backtracking()

                        result = min(result, candidate_value + 1)
                        
                        # retore grid before calling backtracking()
                        restore_from_copy(grid_copy, row, col) 

            return result
        
        return backtracking()

        


