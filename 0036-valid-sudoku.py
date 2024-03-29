
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
    	

    	# check each row and col
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
            # why return true here?
            # 当这层没有办法再走下去的时候, for example: 6 surrounded by visited cell and '.'
            # 返回上一层 5 and go right to 3..
            return True   

        # why loop here?
        # 没有办法走下去时返回到最顶层，但是还没有走完其他的cell
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in cells and board[i][j] != '.':
                    if not dfs(i, j):
                        return False
        return True



