"""
To make sure that we only place 1 queen per row, we will pass an integer argument row into backtrack, and will only place one queen during each call.
To make sure we only place 1 queen per column, we will use a set. Whenever we place a queen, we can add the column index to this set.
For each square on a given diagonal, the difference between the row and column indexes (row - col) will be constant 0.
For each square on a given anti-diagonal, the sum of the row and column indexes (row + col) will be constant.
In the same way we had a set for the column, we should also have a set for both the diagonals and anti-diagonals.
Time complexity: O(N!), O(NxN!)?
Space: O(N^2)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diags, antidiags, cols):
            if row == n: # done placing
                return 1

            solutions = 0
            for col in range(n):
                diag = row - col
                antidiag = row + col
                # if the queen is not placeable
                if (col in cols or diag in diags or antidiag in antidiags):
                    continue
                # add the queen in the board
                cols.add(col)
                diags.add(diag)
                antidiags.add(antidiag)
                # move on to the next row
                solutions += backtrack(row+1, diags, antidiags, cols)
                # remove the queen from the board since we already explored all possible placements using the above call
                cols.remove(col)
                diags.remove(diag)
                antidiags.remove(antidiag)

            return solutions
                
        return backtrack(0, set(), set(), set())
                
if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(4)) # 2
    










    

