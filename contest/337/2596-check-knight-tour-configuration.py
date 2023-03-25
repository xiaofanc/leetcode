"""
There is a knight on an n x n chessboard. In a valid configuration, the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

You are given an n x n integer matrix grid consisting of distinct integers from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

Return true if grid represents a valid configuration of the knight's movements or false otherwise.

Note that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.

Input: grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
Output: true

"""
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        moves = dict()
        for i in range(n):
            for j in range(n):
                moves[grid[i][j]] = (i,j)
        
        def valid(pi, pj, i, j):
            if 0 <= i < n and 0 <= j < n and ((abs(i-pi) == 2 and abs(j-pj) == 1) or (abs(i-pi) == 1 and abs(j-pj) == 2)):
                return True
            
        pi, pj = 0, 0
        for m in range(1, n*n):
            if not valid(pi, pj, moves[m][0], moves[m][1]):
                return False
            pi, pj = moves[m][0], moves[m][1]
        return True
                
            
            
                