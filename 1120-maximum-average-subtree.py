
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float("-inf")
        def helper(node):
            # return sum and #nodes for the subtree with root as node
            nonlocal res
            if not node:
                return 0, 0
            leftSum, leftNode = helper(node.left)
            rightSum, rightNode = helper(node.right)
            # for the current node
            s = leftSum + rightSum + node.val
            n = leftNode + rightNode + 1
            res = max(res, s/n)
            return s, n
        
        helper(root)
        return res
            
