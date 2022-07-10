"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")
        def traverse(node):    
            if not node:
                return 0
            l = traverse(node.left)
            r = traverse(node.right)
            # find the max of path sum (l+r+node) need the max of left subtree and max of right subtree
            self.ans = max(self.ans, l+r+node.val) 
            # return max sum for the parent node (left/right subtree)
            return max(l+node.val, r+node.val, 0)  
        traverse(root)
        return self.ans
                
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def helper(node):
            nonlocal res
            # if not root, return 0
            if not node:
                return 0
            # get the max path sum from left subtree
            l = max(0, helper(node.left))
            # get the max path sum from right subtree
            r = max(0, helper(node.right))
            # for the current node, compare the max sum with left+right+node.val
            res = max(res, l+r+node.val)
            
            # return max(left, right) + node.val to the parent and do not return neg value
            return max(l, r) + node.val
            
        helper(root)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum([-10,9,20,null,null,15,7]))
            
        
        
        