class Solution:
	# backtracking: 579/611 passed
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # brute force solution: backtracking
        # move the stones > 1 to the empty cell
        c = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    c += 1
        if c == 0:
            return 0
                
        res = float('inf')
        
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    for ni in range(3):
                        for nj in range(3):
                            if grid[ni][nj] > 1:
                                d = abs(i-ni) + abs(j-nj)
                                grid[i][j] += 1
                                grid[ni][nj] -= 1
                                res = min(res, d + self.minimumMoves(grid))
                                grid[i][j] -= 1
                                grid[ni][nj] += 1
        return res

class Solution:
	# BFS: Time: O(9!)
    def findNeighbors(self, i):
        r, c = i//3, i%3
        for rr, cc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]: 
            if 0 <= rr < 3 and 0 <= cc < 3: yield rr*3+cc

    def minimumMoves(self, g):
        flatten_g = [g[i//3][i%3]  for i in range(9)]
        queue, visited, target, step = deque([flatten_g]), set(tuple(flatten_g)), [1]*9, 0
        while queue:
            next_level = []
            for g in queue:
                if g == target:
                    return step
                for i in range(9):
                    if g[i] > 1:
                        for nei in self.findNeighbors(i):
                            updated = g[:]
                            updated[i] -= 1
                            updated[nei] += 1
                            if tuple(updated) not in visited:
                                visited.add(tuple(updated))
                                next_level.append(updated)
            queue = next_level
            step += 1
        return step
                
                            


