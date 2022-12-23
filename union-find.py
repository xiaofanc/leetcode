"""
Union Find:
- find the final root of two nodes
- union: add smaller tree to the bigger tree
- each union will decrease cc by 1

323. Number of Connected Components in an Undirected Graph

"""
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # every node is its own parent
    par = [i for i in range(n)]
    # keep track of the weight/size of the tree
    rank = [1 for i in range(n)]
    def find(n):
        if n == par[n]:
            return n
        while n != par[n]:
            par[n] = par[par[n]] # 压缩路径
            n = par[n] # grandparant
        return n
    def union(p1, p2):
        # find the base root of nodes
        r1, r2 = find(p1), find(p2)
        # no need to union
        if r1 == r2:
            return 0
        # else union two trees
        # add small tree to large tree to make the tree balanced
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

class UnionFind:
    def __init__(self, n):
        self.count = n
        # every node is its own parent
        self.par = [i for i in range(n)]
        # keep track of the weight/size of the tree
        self.rank = [1 for i in range(n)]

    def find(self, x):
        # find the root of x
        if x == self.par[x]:
            return x
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]] # 压缩路径
            x = self.par[x] # grandparant
        return x

    def union(self, p1, p2):
        # find the base root of nodes
        r1, r2 = self.find(p1), self.find(p2)
        # no need to union
        if r1 == r2:
            return
        # else union two trees
        # add small tree to large tree to make the tree balanced
        if self.rank[r1] > self.rank[r2]:
            self.par[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.par[r1] = r2
            self.rank[r2] += self.rank[r1]
        self.count -= 1

    def connected(self, p1, p2):
        r1, r2 = self.find(p1), self.find(p2)
        return r1 == r2

    def returnCC(self):
        # return number of connect components
        return self.count


    