"""
n nodes, undirected edges provided
Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.
The price sum of a given path is the sum of the prices of all nodes lying on that path.
Additionally, you are given a 2D integer array trips, where trips[i] = [starti, endi] indicates that you start the ith trip from the node starti and travel to the node endi by any path you like.

Before performing your first trip, you can choose some non-adjacent nodes and halve the prices.
Return the minimum total price sum to perform all the given trips.

Solution:
Since it is a tree -> no cycle, only one path for each pair
So we compute all paths first, and keep counting how many times each node is used.
To find the maximum cost we can reduce, we can use dp to check which is the optimal combinations of reducing the node cost so far.
"""

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # get the count of each node visited in all paths and calculate the total cost without reduction
        # calculate the max reduction with the count using dp
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        count = collections.Counter()
        totalcost = 0
        def dfs(i, par, dest):
            nonlocal count, totalcost
            if i == dest:  # only count for the path from src to dest
                return True
            for nei in adj[i]:
                if nei != par:
                    if dfs(nei, i, dest):
                        count[nei] += 1
                        totalcost += price[nei]
                        return True
            return False
        
        for a, b in trips:
            count[a] += 1
            totalcost += price[a]
            dfs(a, -1, b)
        
        @cache
        def dfs(i, par, canreduce):
            totalreduce = 0
            if canreduce:
                totalreduce += count[i] * (price[i]//2)
            red = 0
            # multiple paths and levels
            for nei in adj[i]:
                if nei != par:
                    if canreduce:
                        cur = dfs(nei, i, False)
                    else:
                        cur = max(dfs(nei, i, False), dfs(nei, i, True))
                    red += cur
            return totalreduce + red

        # find the maximum reduction starting from any node
        reduction = 0
        for i in range(n):
            reduction = max(reduction, dfs(i, -1, True), dfs(i, -1, False))
        return totalcost - reduction









