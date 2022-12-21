class Solution:
    # greedy does not work
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        group = [[1]]
        for i in range(2, n+1):
            for g in group:
                include = True
                for n in g:
                    if n in adj[i]:
                        include = False
                        break
                if include:
                    g.append(i)
                    break
            if not include:
                group.append([i])
        return len(group) <= 2


    # 5, [[1,2],[3,4],[4,5],[3,5]]
    # BFS, assign neighbors different color. If conflict, return False
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        

        colors = [-1]*(n+1)

        def bfs(start):
            q = deque()
            q.append((start))
            colors[start] = 0
            while q:
                i = q.popleft()
                for nei in adj[i]:
                    if colors[nei] == -1:
                        colors[nei] = 1-colors[i]
                        q.append((nei))
                    elif colors[nei] == colors[i]:
                        return False
            return True
        
        # split each connected component to 0 and 1 using BFS
        for i in range(1, n+1):
            if colors[i] == -1:
                if not bfs(i):
                    return False
        return True   

    # DFS
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        colors = [-1]*(n+1)

        def dfs(i, color):
            colors[i] = color
            for nei in adj[i]:
                if colors[nei] == -1:
                    if not dfs(nei, 1-color):
                        return False
                elif colors[nei] == color:
                    return False
            return True
        
        # split each connected component to 0 and 1 using DFS
        for i in range(1, n+1):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        return True   




