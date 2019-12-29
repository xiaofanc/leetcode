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
            self.ans = max(self.ans, l+r+node.val) # find the max of path sum
            return max(l+node.val, r+node.val, 0)  # return max sum for parent node
        traverse(root)
        return self.ans
                
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum([-10,9,20,null,null,15,7]))
            
        
        
        