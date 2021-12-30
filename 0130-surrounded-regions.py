class Solution:
    # Time: O(n), Space: O(n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # when "O" is connected to the "O" on the board
        # we will not change it to "X"

        height, width = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        borders = set()
        # step 1: retrieve all border cells
        # borders = list(product(range(height), [0, width-1])) + list(product([0, height-1], range(width)))
        for i in range(height):
            borders.add((i, 0))
            borders.add((i, width-1))
        for j in range(width):
            borders.add((0, j))
            borders.add((height-1, j))
        
        def dfs(x, y):
            if 0 <= x < height and 0 <= y < width and board[x][y] == "O":
                board[x][y] = "E"
                for dx, dy in directions:
                    dfs(x+dx, y+dy)
                                
        # step 2: mark the escaped cells with 'E'
        for x, y in borders:
            dfs(x, y)
        
        # step 3: flip the captured cells ('O'->'X') and the escaped cells ('E'->'O')
        for i in range(height):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"

# BFS
from itertools import product

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height, width = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # step 1: retrieve all border cells
        borders = list(product(range(height), [0, width-1])) + list(product([0, height-1], range(width)))
        
        def bfs(borders):
            while borders:
                new = []
                for x, y in borders:
                    if 0 <= x < height and 0 <= y < width and board[x][y] == "O":
                        board[x][y] = "E"
                        for dx, dy in directions:
                            new.append((x+dx, y+dy))
                borders = new
                                
        # step 2: mark the escaped cells with 'E'
        bfs(borders)
        
        # step 3: flip the captured cells ('O'->'X') and the escaped cells ('E'->'O')
        for i in range(height):
            for j in range(width):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
 
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









