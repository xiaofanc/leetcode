"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

#DFS

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:  # time O(n)
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            v = node.val
            if v <= lower or v >= upper:
                return False
            
            if not helper(node.left, lower, v):  # leftsubtree < root.val
                return False
            if not helper(node.right, v, upper): # rightsubtree > root.val
                return False
            return True
        return helper(root)


    # stack
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: 
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue  # !!! not return True
            v = root.val
            if v <= lower or v >= upper:
                return False
            stack.append((root.left, lower, v))
            stack.append((root.right, v, upper))
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST([10,5,15,null,null,6,20]))  #false



    