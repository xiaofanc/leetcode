# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        level = deque([root])
        while level:
            size = len(level)
            res = []
            for i in range(size):
                node = level.popleft()
                res.append(node.val)
                for c in [node.left, node.right]:
                    if c:
                        level.append(c)
                # level = [c for node in level for c in [node.left, node.right] if c]
        return res[0]

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        level = [root]
        while level:
            res = [node.val for node in level]
            level = [c for node in level for c in [node.left, node.right] if c]
        return res[0]