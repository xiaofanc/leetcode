"""
for each box: index = i//3 * 3 + j//3
"""

class Solution:
	# Time: O(N^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                
                x = i//3 * 3 + j//3
                if board[i][j] in boxes[x]:
                    return False
                boxes[x].add(board[i][j])
        return True

    # Initialize an array of size N filled with zeros for each row, column, and box, where N is the sudoku board length, which is 9 in this case.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        boxes = [[0]*N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                val = board[i][j]
                if val == '.':
                    continue
                
                pos = int(val)-1
                if rows[i][pos] == 1:
                    return False
                rows[i][pos] = 1
                
                if cols[j][pos] == 1:
                    return False
                cols[j][pos] = 1
                
                x = i//3 * 3 + j//3
                if boxes[x][pos] == 1:
                    return False
                boxes[x][pos] = 1
                
        return True
                    
if __name__ == '__main__':
	s = Solution()
	print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))  # False
