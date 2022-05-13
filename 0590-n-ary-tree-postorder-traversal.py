"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # iterative
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:  # [中，左，右] pop -> [中，右，左] reverse -> [左，右，中]
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack.extend(node.children)
        return res[::-1]

    # recursion
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(node):
            if not node:
                return
            for c in node.children: # [左，右，中]
                helper(c)
            res.append(node.val)
        helper(root)
        return res