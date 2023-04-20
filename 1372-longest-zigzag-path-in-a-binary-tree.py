"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, path, left):
            # path = longestZigZag ends at node
            # left = current node is left child or not
            nonlocal res
            res = max(res, path)
            if left:
                if node.right: dfs(node.right, path+1, False)
                if node.left: dfs(node.left, 1, True)
            else:
                if node.left: dfs(node.left, path+1, True)
                if node.right: dfs(node.right, 1, False)
        if not root:
            return 0
        if root.left: dfs(root.left, 1, True)
        if root.right: dfs(root.right, 1, False)
        return res

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, path, left):
            nonlocal res
            res = max(res, path)
            if not node:
                return
            if left:
                dfs(node.right, path+1, False)
                dfs(node.left, 0, True)
            else:
                dfs(node.left, path+1, True)
                dfs(node.right, 0, False)
        if not root:
            return 0
        dfs(root.left, 0, True)
        dfs(root.right, 0, False)
        return res

        

            


