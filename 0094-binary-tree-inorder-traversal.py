# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        def pushleft(node):
            # in order to pop left node first
            while node:
                stack.append(node)
                node = node.left
        pushleft(root) #root, root.left, root.left.left...
        while stack:
            top = stack.pop()   # node.left
            ans.append(top.val) # node.left
            pushleft(top.right) # node.left.right
        return ans
            
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal([1,null,2,3]) == [1, 3, 2])