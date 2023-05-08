"""
You are given an integer n representing the number of nodes in a perfect binary tree consisting of nodes numbered from 1 to n. The root of the tree is node 1 and each node i in the tree has two children where the left child is the node 2 * i and the right child is 2 * i + 1.

Each node in the tree also has a cost represented by a given 0-indexed integer array cost of size n where cost[i] is the cost of node i + 1. You are allowed to increment the cost of any node by 1 any number of times.

Return the minimum number of increments you need to make the cost of paths from the root to each leaf node equal.

method:
Bottom up iterate the whole tree.
For each node i, compare its two children left and right.
The smaller child needs to catch up the bigger child,
so we increment res += abs(A[left] - A[right]),
then we update A[i] += max(A[left], A[right],
and A[i] present minimum cost from node i to any leaf.

We continue iterate the whole tree and finally return result res
"""

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # res += abs(left-right) to make the subtree same cost
        # return max(left, right) + root cost to the parent
        if n <= 1:
            return 0
        paths = [0]*n
        res = 0
        def isleaf(i):
            if 2*i+1 >= n:
                return True
            return False

        for i in range(n-1,1,-2):
            if i % 2 == 0:
                p = (i-1) // 2
            else:
                p = i // 2
            left, right = 2*p+1, 2*p+2
            if isleaf(left):
                paths[left] = cost[left]
            if isleaf(right):
                paths[right] = cost[right]
            res += abs(paths[left]-paths[right])
            paths[p] = max(paths[left], paths[right]) + cost[p]
            # print("paths ", paths)
            # print("res ", res)
        return res
            
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # res += abs(left-right) to make the subtree same cost
        # return max(left, right) + parent cost to the parent
        if n <= 1:
            return 0
        res = 0
        for i in range(n//2-1,-1,-1): # non-leaf
            left, right = 2*i+1, 2*i+2
            res += abs(cost[left]-cost[right])
            cost[i] += max(cost[left], cost[right])
            # print("cost, ", cost)
        return res

    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        def dfs(i):
            nonlocal res
            if i >= n:
                return 0
            l, r = dfs(2*i+1), dfs(2*i+2)
            res += abs(l-r)
            return max(l,r) + cost[i]
        dfs(0)
        return res
            
            
        
        
        