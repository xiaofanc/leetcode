"""
Union Find:
- find the final root of two nodes
- union: add smaller tree to the bigger tree
- each union will decrease cc by 1

323. Number of Connected Components in an Undirected Graph

"""
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




    