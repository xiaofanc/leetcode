
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        level = [root]
        while level:
            depth += 1
            level = [child for node in level for child in node.children]
        return depth
                
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(self.maxDepth(child), depth)
        return depth + 1

    def maxDepth(self, root: 'Node') -> int:
        res = 0
        if not root:
            return res
        def getDepth(node):
            if not node:
                return 0
            depth = 0
            for child in node.children:
                depth = max(depth, getDepth(child))
            return depth + 1
        res = getDepth(root)
        return res




        