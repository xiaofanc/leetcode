"""
connect nodes for a binary tree

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        frontier = [root]
        while frontier:
            for i in range(len(frontier)-1):
                frontier[i].next = frontier[i+1]
            frontier = [n for f in frontier for n in (f.left, f.right) if n]
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        res = []
        def helper(node, depth):
            if len(res) == depth:
                res.append([])
            # if res[depth] != []:              does not work
            #     res[depth][-1].next = node
            res[depth].append(node)
            if node.left:
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        helper(root, 0)
        for lst in res:
            for i in range(len(lst)-1):
                lst[i].next = lst[i+1]
        return root
