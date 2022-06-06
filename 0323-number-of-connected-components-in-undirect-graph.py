"""
return number of connected components in the graph
	- DFS to visit nodes in the same cc
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        if not n:
            return 0
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        # keep track of visited nodes
        visited = set()
        def dfs(n, prev):
            if n in visited:  # cycle
                return
            
            visited.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue
                dfs(nei, n)
        res = 0
        for i in range(n):
            if i in visited: 
                continue
            else:
                res += 1
                dfs(i, -1)
        return res

    # union - find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # every node is its own parant
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        def find(n):
            if n == par[n]:
                return n
            while n != par[n]:
                par[n] = par[par[n]] # optimize
                n = par[n] # grandparant
            return n
        def union(p1, p2):
        	# find the base root of nodes
            r1, r2 = find(p1), find(p2)
            if r1 == r2:
                return 0
            # else union two trees
            if rank[r1] > rank[r2]:
                par[r2] = r1
                rank[r1] += rank[r2]
            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            return 1
        res = n
        for a, b in edges:
            res -= union(a, b)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.countComponents(5, [[0,1],[1,2],[3,4]]))  # 2



