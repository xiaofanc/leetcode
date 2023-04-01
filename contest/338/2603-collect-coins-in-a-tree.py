class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        ones = sum(coins)
        res = float('inf')
        
        def findcoins(i):
            stack = set()
            stack.add(i)
            res = coins[i]
            
            for j in adj[i]:
                stack.add(j)
            for node in stack:
                res += coins[node]
            return stack, res
            
        def dfs(i, coin, step, visited):
            nonlocal res
            if i in visited:
                return
            if coin == ones:
                res = min(res, step * 2)
                print("done: ", res)
            
            for nei in adj[i]:
                if nei not in visited:
                    print("nei: ", nei)
                    v, c = findcoins(nei)
                    print("v, c: ", v, c)
                    visited = visited.union(v)
                    coin += c
                    print("step: ", step)
                    dfs(nei, coin, step+1, visited)
        
        n = len(coins)
        for i in range(n):
            dfs(i, 0, 0, set())
        return res
            
            
            
        