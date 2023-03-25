class Solution:
    # union-find
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(a, b):
            r1, r2 = find(a), find(b)
            if r1 == r2:
                return 0
            if rank[r1] < rank[r2]:
                par[r1] = r2
                rank[r2] += rank[r1]
            else:
                par[r2] = r1
                rank[r1] += rank[r2]
            return 1
        
        for a, b in edges:
            union(a, b)
        
        # count number of nodes in each cc
        count = collections.Counter()
        for i in range(n):
            # find(i) to get the final root
            count[find(i)] += 1

        res = 0
        leftnodes = n
        for k, size in count.items():
            res += size * (leftnodes - size)
            leftnodes -= size
        
        return res

    # DFS
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False]*n
        def dfs(i):
            # count number of nodes in each cc
            visited[i] = True
            cnt = 1
            for nei in adj[i]:
                if not visited[nei]:
                    cnt += dfs(nei)
            return cnt
        
        # number of nodes in each cc
        comps = [] 
        for i in range(n):
            if not visited[i]:
                count = dfs(i)
                comps.append(count)

        res = 0
        leftnodes = n
        for size in comps:
            # each node in a cc is unreachable from the left nodes
            res += size * (leftnodes - size)
            leftnodes -= size
        
        return res

    # BFS
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False]*n
        def bfs(i):
            # count number of nodes for one cc
            visited[i] = True
            queue = deque()
            queue.append(i)
            size = 1

            while queue:
                i = queue.popleft()
                for nei in adj[i]:
                    if not visited[nei]:
                        size += 1
                        visited[nei] = True
                        queue.append(nei)
            return size
        
        res = 0
        leftnodes = n
        for i in range(n):
            if not visited[i]:
                cc_size = bfs(i)
                res += cc_size  * (leftnodes - cc_size)
                leftnodes -= cc_size

        return res







            