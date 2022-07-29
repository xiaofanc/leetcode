
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        # check 3x3 subboxes
        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                visited = set()
                for m in range(3):
                    for n in range(3):
                        # print("checking", m+i, n+j, visited)
                        if board[m+i][n+j] not in visited and board[m+i][n+j] != '.':
                            visited.add(board[m+i][n+j])
                        elif board[m+i][n+j] == '.':
                            continue
                        else:
                            return False
                        # print("checking", visited)
    
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        row = [set() for i in range(rows)]
        col = [set() for i in range(cols)]
        cells = set()
        def dfs(i, j):
            # print("i, j", i, j, board[i][j], row[i], col[j])
            if board[i][j] != '.' and (board[i][j] in row[i] or board[i][j] in col[j]):
                return False
            cells.add((i,j))
            row[i].add(board[i][j])
            col[j].add(board[i][j])
            for dx, dy in dirs:
                if i+dx == rows or i+dx < 0 or j+dy == cols or j+dy < 0 or (i+dx,j+dy) in cells:
                    continue
                if not dfs(i+dx, j+dy):
                    return False
            return True
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in cells and board[i][j] != '.':
                    if not dfs(i, j):
                        return False
        return True
