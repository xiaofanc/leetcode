"""
How to avoid the matrix again and again?
"""
class Solution:
	# TLE 17/21
    def maxPoints(self, grid: List[List[int]], q: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        
        def dfs(i, j, target):
            if i < 0 or i == rows or j < 0 or j == cols or (i, j) in visited or grid[i][j] >= target:
                return
            visited.add((i, j))
            for dx, dy in dirs:
                dfs(i+dx, j+dy, target)
        
        res = []
        for i in range(len(q)):
            visited = set()
            dfs(0, 0, q[i])
            res.append(len(visited))
        return res

    def maxPoints(self, grid: List[List[int]], q: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        count = dict() # map q to count

        # sort query to avoid reading grid multiple times
        qs = sorted(q)

        # use minheap to keep track of the cells that reachable
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))

        cnt = 0
        visited = set()
        visited.add((0,0))

        # Time: O(QMNlogMN)
        for i in qs:
            while heap and heap[0][0] < i:
                cur, x, y = heapq.heappop(heap)
                cnt += 1
                for dx, dy in dirs:
                    if 0 <= x+dx < rows and 0 <= y+dy < cols and (x+dx, y+dy) not in visited:
                        visited.add((x+dx, y+dy))
                        heapq.heappush(heap, (grid[x+dx][y+dy], x+dx, y+dy))
            count[i] = cnt
        
        return [count[i] for i in q]


    # Time: O((MN+Q)logMN)
    def maxPoints(self, grid: List[List[int]], q: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        order = [] 
        visited = set()
        visited.add((0,0))

        # keep track of reaching order of the cells
        while heap:
            cur, x, y = heapq.heappop(heap)
            order.append(cur)
            for dx, dy in dirs:
                if 0 <= x+dx < rows and 0 <= y+dy < cols and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    heapq.heappush(heap, (grid[x+dx][y+dy], x+dx, y+dy))
        
        maxv = float('-inf')
        for i in range(len(order)):
            # max value to reach the current cell
            maxv = max(maxv, order[i])
            order[i] = maxv
        
        res = []
        for i in q:
            # find the first value >= i
            res.append(bisect.bisect_left(order, i))
        return res


            
                
            