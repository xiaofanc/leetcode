"""
Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:

Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
He tells Alice that u is the parent of v in the tree.
Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.

Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.

Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.
"""

class Solution:
    # BFS: 37 / 51 test cases passed.
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        n = len(edges)+1
        guesses = set([(a,b) for a,b in guesses])
        res = 0
        for i in range(n):
            correct = 0
            queue = deque()
            queue.append(i) # root
            visited = set()
            visited.add(i)
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    if (node, nei) in guesses:
                        correct += 1
                    visited.add(nei)
                    queue.append(nei)
            if correct >= k:
                res += 1
        return res

    # DFS with cache
    def rootCount(self, edges: List[List[int]], guess: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        guess = set([(u,v) for u,v in guess])

        @cache    
        def dfs(node, par):
            if node in visited:
                return
            visited.add(node)
            res = 0
            for nei in adj[node]:
                if nei != par:
                    res += int((node, nei) in guess)
                    res += dfs(nei, node)
            return res
        
        res = 0
        for i in range(n):
            visited = set()
            if dfs(i, -1) >= k:
                res += 1
        return res

    # rerooting
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        child = defaultdict(set)
        for u, v in guesses:
            child[u].add(v)

        # fill parent for tree rooted as 0
        # and calculate total correct guesses for the tree rooted as 0
        parents = {}
        total_guess = 0
        def fill_parent(node, par):
            nonlocal total_guess
            parents[node] = par
            for nei in adj[node]:
                if nei != par:
                    if nei in child[node]:
                        total_guess += 1
                    fill_parent(nei, node)
        
        fill_parent(0, -1)
        res = 0

        # next update the total_guess by rerooting at node [1,n]
        def dfs(node, par, correct_guess):
            nonlocal res
            cur = correct_guess
            if node in child[par]:
                cur -= 1
            if par in child[node]:
                cur += 1
            if cur >= k:
                res += 1
            for nei in adj[node]:
                if nei != par:
                    dfs(nei, node, cur)
        dfs(0, -1, total_guess)
        return res

            