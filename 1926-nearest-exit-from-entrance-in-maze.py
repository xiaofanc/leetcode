class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        exits = set()
        visited = set()
        # print("rows, cols", rows, cols)
        for i in range(rows):
            for j in range(cols):
                # print(i, j, maze[i][j])
                if maze[i][j] == "." and (i != entrance[0] or j != entrance[1]) and (i == rows-1 or i == 0 or j == cols-1 or j == 0):
                    exits.add((i, j))
                if maze[i][j] == "+":
                    visited.add((i, j))

        # print("exits, ", exits)
        queue = collections.deque([])
        queue.append(tuple(entrance))
        visited.add(tuple(entrance))
        step = 0
        while queue:
            # print("queue ->", queue)
            size = len(queue)
            for i in range(size):
                a, b = queue.popleft()
                if (a,b) in exits:
                    return step
                for (dx, dy) in dirs:
                    if a+dx >= 0 and a+dx < rows and b+dy >= 0 and b+dy < cols and (a+dx, b+dy) not in visited:
                        queue.append((a+dx, b+dy))
                        visited.add((a+dx, b+dy))
            step += 1
        return -1



