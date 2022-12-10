# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

class Solution:
    # two-pass DFS
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        def inorder(node):
            nonlocal total
            if not node:
                return
            inorder(node.left)
            total += node.val
            inorder(node.right)
        inorder(root)

        res = float('-inf')
        def subtreeSum(node, total):
            nonlocal res
            if not node:
                return 0
            left = subtreeSum(node.left, total)
            right = subtreeSum(node.right, total)
            subsum = left + right + node.val
            res = max(res, subsum*(total-subsum))
            return subsum
        
        subtreeSum(root, total)
        return res % (10**9+7)

    # one-pass DFS
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        treesums = []

        def treeSum(node):
            if not node:
                return 0
            left = treeSum(node.left)
            right = treeSum(node.right)
            subsum = left + right + node.val
            treesums.append(subsum)
            return subsum
        
        total = treeSum(root)
        res = float('-inf')
        for s in treesums:
            res = max(res, s*(total-s))
        return res % (10**9+7)




            
