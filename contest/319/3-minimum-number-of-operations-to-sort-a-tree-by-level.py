"""
Given an array of n distinct elements, find the minimum number of swaps required to sort the array:
The graph will now contain many non-intersecting cycles. Now a cycle with 2 nodes will only require 1 swap to reach the correct ordering, similarly, a cycle with 3 nodes will only require 2 swaps to do so. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = [root]
        res = 0
        while level:
            nodes = [node.val for node in level]
            sortedNodes = sorted(nodes)
            cur = {num:i for i, num in enumerate(nodes)}
            pos = {num:i for i, num in enumerate(sortedNodes)}
            visited = set()
            for i, n in enumerate(nodes):
                if n in visited:
                    continue
                cycle = [] # find cycle starts from n
                while n not in visited:
                    if pos[n] == cur[n]: # no cycle
                        break
                    cycle.append(n)
                    visited.add(n)
                    n = nodes[pos[n]] # next node in the cycle
                if len(cycle) > 0: 
                    res += len(cycle)-1
            level = [c for node in level for c in (node.left, node.right) if c]
        return res
                
                    
                    
            