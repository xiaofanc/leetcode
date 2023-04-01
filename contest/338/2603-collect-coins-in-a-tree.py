"""
https://leetcode.com/problems/collect-coins-in-a-tree/solutions/3345266/trim-leaves/

We can trim leaves from the tree using BFS. We trim all leaves before trimming a branch, using counter cnt to track remaining edges.
If a branch does not have coins, we can trim it freely (gray edges).
However, once we see a coin for the first time, we can trim up to 2 levels of leaves (red edges).

In the end, we will have a subtree that we cannot trim anymore, containing m nodes.
Because it's a tree (and not a graph), this subtree will have m - 1 edges (green in the picture above).
It does not matter how we choose a starting node - it will take 2 * (m - 1) steps to visit all nodes and get back.
"""

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        deleted = 0

        # remove leaf with zero coins
        n = len(coins)
        leaves = []
        for i in range(n):
            u = i
            while len(adj[u]) == 1 and coins[u] == 0:
                # remove edge
                v = adj[u].pop()
                adj[v].remove(u)
                deleted += 1
                u = v
            if len(adj[u]) == 1: # remaining leaves with coins
                leaves.append(u)

        # all remaining leaves have coins, we can trim up to 2 levels of leaves
        for l in range(0,2):
            temp = []
            for u in leaves:
                # coins = [1,1], edges = [[0,1]]
                # adj[u] is changing, so we need to check again
                if len(adj[u]) == 1: 
                    v = adj[u].pop()
                    adj[v].remove(u)
                    deleted += 1
                    if len(adj[v]) == 1:
                        temp.append(v)
            leaves = temp
        
        # In the end, we will have a subtree that we cannot trim anymore.
        return (len(edges) - deleted) * 2






