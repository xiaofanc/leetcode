"""
BFS to find the shortest path
"""
class Solution:
	# Time: O(MxN)
    def getFood(self, grid: List[List[str]]) -> int:
        # use bfs to find the shorted path the get the food
        queue = deque()
        visited = set()
        # find where you are, add the position and depth into deque
        # add start position to the visited set
        rows, cols = len(grid), len(grid[0])     
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i, j, 0))
                    visited.add((i, j))
                    break
        # while deque, pop one element from deque
        while queue:      
            i, j, depth = queue.popleft()
            # if the element is food cell return depth
            if grid[i][j] == '#':
                return depth
            # else add neighbors into deque if in the bound and free space
            for dx, dy in dirs:
                if i+dx < 0 or j+dy < 0 or i+dx == rows or j+dy == cols or (i+dx, j+dy) in visited:
                    continue
                if grid[i+dx][j+dy] == 'X':
                    visited.add((i+dx, j+dy))
                    continue
                visited.add((i+dx, j+dy))
                queue.append((i+dx, j+dy, depth+1))
        # if we cannot reach food, return -1
        return -1

if __name__ == '__main__':
	s = Solution()
	print(s.getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]))  # 3

