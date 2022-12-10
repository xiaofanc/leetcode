# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def preorder(node, maxa, mina):
            nonlocal res
            if not node:
                return
            res = max(res, abs(maxa-node.val), abs(mina-node.val))
            maxa = max(maxa, node.val)
            mina = min(mina, node.val)
            preorder(node.left, maxa, mina)
            preorder(node.right, maxa, mina)
        preorder(root, root.val, root.val)
        return res
            