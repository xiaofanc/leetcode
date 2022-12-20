from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def place_next_number(row, col):
            """
            Call backtrack function in recursion
            """
            if col == N-1 and row == N-1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N-1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)
                    
        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'
            
        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)
            
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n
        # init row, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = 9, 9

        def isValid(r, c, n):
            for i in range(9):
                if board[r][i] == n:
                    return False
                if board[i][c] == n:
                    return False
                if board[r//3*3+i//3][c//3*3+i%3] == n:
                    return False
            return True

        def backtrack(i, j):
            # if col is placed, place next row
            if j == 9:
                return backtrack(i+1, 0)
            # if all rows are placed, then solved
            if i == 9:
                return True
            # if cannot be placed, move to the next position
            if board[i][j] != ".":
                return backtrack(i, j+1)
            
            # select from all possible candidates
            for n in range(1, 10):
                if not isValid(i, j, str(n)):
                    continue
                board[i][j] = str(n)
                if backtrack(i, j+1):
                    return True
                board[i][j] = "."
            return False

        return backtrack(0, 0)

        




        