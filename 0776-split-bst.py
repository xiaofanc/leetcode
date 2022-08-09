# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def splitBST(self, root, V):
        # return the parts after split
        if not root:
            return None, None
        elif root.val <= V:
            # split the right subtree
            bns = self.splitBST(root.right, V)  
            root.right = bns[0]
            return root, bns[1]
        else:
            # split the left subtree
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root
