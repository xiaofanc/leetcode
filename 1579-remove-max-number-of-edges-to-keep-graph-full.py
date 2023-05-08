"""
Since we need the minimum number of edges to connect all the nodes, the Type 3 edges are the most useful as one Type 3 edge adds two edges, one for Alice and one for Bob. Hence, we will first iterate over the edges of Type 3, and for these edges we will add the edge to both graphs.

perform union of edges of type 3, increment the value of required if the edge connect two nodes that are not connected
perform union of edges of type 1 & 2 for Alice or Bob respectively and increase required by 1 if the edge connect two nodes that are not connected
check if the graph is connect for Alice and Bob, return total edges - required if True, else return -1
"""

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [1 for i in range(n+1)]
        self.components = n
    
    def find(self, node):
        while node != self.par[node]:
            node = self.par[node]
        return node
    
    def union(self, p, q):
        r1, r2 = self.find(p), self.find(q)
        if r1 == r2:
            return False
        if self.rank[r1] < self.rank[r2]:
            self.par[r1] = r2
            self.rank[r2] += self.rank[r1]
        else:
            self.par[r2] = r1
            self.rank[r1] += self.rank[r2]
        self.components -= 1
        return True

    def isGConnect(self):
        return self.components == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = UnionFind(n)
        B = UnionFind(n)
        required = 0
        for edge in edges:
            # Perform union for edges of type = 3, for both Alice and Bob.
            if edge[0] == 3:
                required += A.union(edge[1], edge[2])
                B.union(edge[1], edge[2])
        
        for edge in edges:
        	# perform union of edges of type 1 & 2 for Alice or Bob respectively
            if edge[0] == 1:
                required += A.union(edge[1], edge[2])

            elif edge[0] == 2:
                required += B.union(edge[1], edge[2])

        # check if both is connected
        if A.isGConnect() and B.isGConnect():
            return len(edges)-required
        return -1





