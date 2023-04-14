"""
DFS: TLE
Since we need to find the shortest cycle, no need to check all cycles

BFS:
Compare the shortest cycle rooting from each node
"""

class Solution:
    # TLE: 61/88 passed
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = float('inf')
        def dfs(i, prev, pos):
            nonlocal res
            if i in indexes:
                # 0-1-2-3-1
                res = min(res, pos-indexes[i])
                return
            indexes[i] = pos
            nodes.add(i)
            for nei in adj[i]:
                if nei != prev:
                    dfs(nei, i, pos+1)
            del indexes[i]
        
        nodes = set()
        for i in range(n):
            if i not in nodes:
                indexes = {}
                dfs(i, -1, 0)
        if res == float('inf'):
            return -1
        return res


    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        res = float('inf')
        def bfs(i):
            # print("i, ", i)
            # find the shorted cycle starting from i
            queue = deque()
            queue.append((i,-1,0))
            while queue:
                # d = distance from root i
                node, prev, d = queue.popleft()
                dist[node] = d
                # nodes.add(node)
                for nei in adj[node]:
                    if nei != prev:     # do not go back to the parent
                        if nei in dist: # meet the node in the same cycle, it is the shorted cycle starting from i
                            return d + 1 + dist[nei]
                        queue.append((nei, node, d+1))
                        # print("queue ", queue)
            return float('inf')

        # nodes = set()
        # why we want to check cycle starting from each node?
        # 0-1-2-3-1
        # we start from 0, res = 5, we start from 1, res = 3
        # otherwise, we need to find the root of the cycle -> 1
        for i in range(n):
            # if i not in nodes:
            dist = {}
            res = min(res, bfs(i))
        if res == float('inf'):
            return -1
        return res
                
                
        
