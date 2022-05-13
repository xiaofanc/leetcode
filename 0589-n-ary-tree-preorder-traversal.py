"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        return 'N(%s,%s)' % (self.val, self.children or '')

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(node):
            if not node:
                return None
            res.append(node.val)
            for c in node.children:
                helper(c)
        helper(root)
        return res

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:  # [中，右，左] pop -> [中，左，右]
                stack.extend(node.children[::-1])
        return res

if __name__ == '__main__':
    N = Node
    root = N(1, N(3, N(5), N(6)), N(2), N(4))
    print("root->", root)
    s = Solution()
    print(s.preorder(root))



