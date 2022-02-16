"""
No need to use grid, just check sum for each row, each col and diag, antidiag
"""

class Solution:
	# Time: O(m)
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        cols = [0] * n
        rows = [0] * n 
        diag = antidiag = 0
        p = [1, -1]
        for i in range(len(moves)):
            row, col = moves[i][0], moves[i][1]
            if i % 2 == 0:
                reward = p[0]
            else:
                reward = p[1]
            rows[row] += reward
            cols[col] += reward
            if row + col == 2:
                antidiag += reward
            if row == col:
                diag += reward
            # check if wins
            if any(abs(line) == n for line in (rows[row], cols[col], diag, antidiag)):
                return "A" if reward == 1 else "B"
            # if 3 in cols or 3 in rows or diag == 3 or antidiag == 3:
            #     return "A"
            # if -3 in cols or -3 in rows or diag == -3 or antidiag == -3:
            #     return "B"
        if i == n*n-1:
            return "Draw" 
        else:
            return "Pending"

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        cols = [0] * n
        rows = [0] * n 
        diag = antidiag = 0
        p = 1
        for i in range(len(moves)):
            row, col = moves[i][0], moves[i][1]
            rows[row] += p
            cols[col] += p
            if row + col == n-1:
                antidiag += p
            if row == col:
                diag += p
            # check if wins
            if any(abs(line) == n for line in (rows[row], cols[col], diag, antidiag)):
                return "A" if p == 1 else "B"
            p *= -1
        if i == n*n-1:
            return "Draw" 
        else:
            return "Pending"
                

if __name__ == '__main__':
	s = Solution()
	print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])) # "A"

	                            
                