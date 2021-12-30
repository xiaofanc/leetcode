class Solution:
    # Time: O(n!), Space: O(n^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
        # A queen can be attacked if another queen is on the same row, column, diagonal, or anti-diagonal
                
        def create_board(board):
            res = []
            for row in board:
                res.append("".join(row))
            return res
        
        # 3 sets that track which columns, diagonals, and anti-diagonals have already had queens placed on them
        def backtrack(row, cols, diagonals, antidiags, board):
            # base case: n queens have been placed
            if row == n:
                ans.append(create_board(board))
                return
            # iterate through the columns of the current row
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # if the queen is not placeable
                if (col in cols) or (curr_diagonal in diagonals) or (curr_anti_diagonal in antidiags):
                    continue
                # else add the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                antidiags.add(curr_anti_diagonal)
                board[row][col] = "Q"
                
                # move on the next row with the updated board state
                backtrack(row+1, cols, diagonals, antidiags, board)
                
                # "Remove" the queen from the board since we have already explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                antidiags.remove(curr_anti_diagonal)
                board[row][col] = "."
            
        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4)) # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

    
            