# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #find the root based on preorder traversal 
        #then find the root in inorder traversal
        #Left is the left subtree, and right is the right subtree
        if inorder == []:
            return None
        pivot = preorder[0]
        i = inorder.index(pivot)
        node = TreeNode(pivot)
        node.left  = self.buildTree(preorder[1:i+1], inorder[0:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])   
        return node
        