class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited and board[i][j] == "O":
                visited.add((i, j))
                for dx, dy in dirs:
                    dfs(i+dx, j+dy)
        
        # get all cells connected with boarder cell "O"
        for j in range(n):
            if board[0][j] == "O": dfs(0, j)
            if board[m-1][j] == "O": dfs(m-1, j)
        
        for i in range(m):
            if board[i][0] == "O": dfs(i, 0)
            if board[i][n-1] == "O": dfs(i, n-1)
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
        return board
 
# BFS - Deque
from itertools import product
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height, width = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # step 1: retrieve all border cells
        borders = list(product(range(height), [0, width-1])) + list(product([0, height-1], range(width)))
        
        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                # BFS - first-in-first-out
                (x, y) = queue.popleft()
                # DFS - last-in-first-out
                # (x, y) = queue.popl()
                if 0 <= x < height and 0 <= y < width and board[x][y] == "O":
                    board[x][y] = "E"
                    for dx, dy in directions:
                        queue.append((x+dx, y+dy))
                                
        # step 2: mark the escaped cells with 'E'
        for x, y in borders:
            bfs(x, y)
        
        # step 3: flip the captured cells ('O'->'X') and the escaped cells ('E'->'O')
        for i in range(height):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
        

if __name__ == '__main__':
    s = Solution()
    print([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) #[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]









