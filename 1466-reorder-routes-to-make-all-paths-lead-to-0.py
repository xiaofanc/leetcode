class Solution:
    # BFS
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        inedges = defaultdict(list)
        outedges = defaultdict(list)

        for a, b in connections:
            outedges[a].append(b)
            inedges[b].append(a)
        
        res = 0
        visited = [False] * n
        queue = deque()
        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.popleft()
            for nei in inedges[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)
            for nei in outedges[node]:
                if not visited[nei]:
                    visited[nei] = True
                    res += 1
                    queue.append(nei)
        return res

    # DFS
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in connections:
            adj[a].append(('to', b))
            adj[b].append(('from', a))
        
        res = 0
        visited = [False] * n
        
        def dfs(i):
            nonlocal res
            visited[i] = True
            for nei in adj[i]:
                if nei[0] == "to" and not visited[nei[1]]:
                    res += 1
                    dfs(nei[1])
                if nei[0] == "from" and not visited[nei[1]]:
                    dfs(nei[1])
        dfs(0)
        return res

                    

