# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def helper(node, val):
            nonlocal res
            if not node.left and not node.right:
                res += val
                return
            if node.left: helper(node.left, 10*val + node.left.val)
            if node.right: helper(node.right, 10*val + node.right.val)
        helper(root, root.val)
        return res


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, val):
            nonlocal res
            if node:
                val = 10 * val + node.val
                if not node.left and not node.right:
                    res += val
                    return
                helper(node.left, val)
                helper(node.right, val)
            
        helper(root, 0)
        return res


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]

        while stack:
            node, val = stack.pop()
            if node:
                val = 10 * val + node.val
                if not node.left and not node.right:
                    res += val
                else:
                    stack.append((node.left, val))
                    stack.append((node.right, val))
        return res



        