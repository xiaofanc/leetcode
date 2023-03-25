class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i, visited, prev, d):
            # print(" "*d, "i -> ", i)
            nonlocal extra
            if i in visited:
                extra += 1
                return
            visited.add(i)
            for nei in adj[i]:
                if nei != prev:
                    # print(" "*d, "nei, extra ", nei, extra)
                    dfs(nei, visited, i, d+1)
            
        extra = 0
        cc = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, visited, -1, 0)
                cc += 1
        if extra//2 >= cc-1:
            return cc-1
        return -1
        
    # DFS
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(i, visited):
            visited[i] = True
            for nei in adj[i]:
                if not visited[nei]:
                    dfs(nei, visited)
            
        cc = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(i, visited)
                cc += 1
        # a connected graph has at least n-1 edges 
        if len(connections) < n-1:
            return -1
        return cc-1

    # BFS
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False]*n
        cc = 0

        def bfs(i, visited): # visited可以不pass
            queue = deque()
            queue.append(i)
            visited[i] = True

            while queue:
                i = queue.popleft()
                for nei in adj[i]:
                    if not visited[nei]:
                        visited[nei] = True
                        queue.append(nei)
        
        for i in range(n):
            if not visited[i]:
                bfs(i, visited)
                cc += 1
        
        if len(connections) < n-1:
            return -1
        return cc-1

    # union-find
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        par = [i for i in range(n)]
        rank = [1 for i in range(n)] # size of the subtree rooted on i
        
        def find(node):
            # find the root of the node
            while node != par[node]:
                par[node] = par[par[node]] # optimize
                node = par[par[node]]
            return node
        
        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return 0
            if rank[root1] > rank[root2]:
                par[root2] = root1
                rank[root1] += rank[root2]
            else:
                par[root1] = root2
                rank[root2] += rank[root1]
            return 1
        
        cc = n
        for a, b in connections:
            # union will reduce 1 cc
            cc -= union(a, b)
        return cc-1



