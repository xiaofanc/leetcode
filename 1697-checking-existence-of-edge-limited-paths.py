
class Solution:
	# 17 / 23 testcases passed
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for a, b, w in edgeList:
            adj[a].append((b,w))
            adj[b].append((a,w))
        
        def dfs(node, end, maxd):
            if node == end:
                return True
            visited.add(node)
            for nei, d in adj[node]:
                if nei not in visited and d < maxd:
                    if dfs(nei, end, maxd):
                        return True
            return False
        
        res = []
        for p, q, limit in queries:
            visited = set()
            if dfs(p, q, limit):
                res.append(True)
            else:
                res.append(False)
        return res

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node

    def union(self, p, q):
        r1, r2 = self.find(p), self.find(q)
        if r1 == r2:
            return True
        if self.rank[r1] > self.rank[r2]:
            self.par[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.par[r1] = r2
            self.rank[r2] += self.rank[r1]
        return False

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
	# add edges one by one when edge weight < limit
	# check if p and q are connected with the current added edges
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # sort edgeList and queries
        # check whether p and q are connected with the edges < limit
        UF = UnionFind(n)
        edgeList.sort(key = lambda x: x[2])

        # add index to queries before sorting for res
        new_queries = []
        for i, q in enumerate(queries):
            new_queries.append(q + [i])
        new_queries.sort(key = lambda x: x[2])

        i = 0
        res = [False] * len(queries)
        for p, q, limit, j in new_queries:
            # add edges < limit to the graph
            while i < len(edgeList) and edgeList[i][2] < limit:
                n1, n2 = edgeList[i][0], edgeList[i][1]
                UF.union(n1, n2)
                i += 1
            # check if p and q are connected in the current graph
            if UF.connected(p, q):
                res[j] = True
        return res





        


