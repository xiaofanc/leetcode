# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #root > R
        #root < L
        #root in [L, R]
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
            
        return trim(root)
        
            
if __name__ == '__main__':
    s = Solution()
    print(s.trimBST([1,0,2], 1, 2) == [1,null,2])