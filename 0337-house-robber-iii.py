# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def trav(node):
            if not node: return (0, 0)
            #node.left level1 and level2
            l1, l2 = trav(node.left)
            #node.right level1 and level2
            r1, r2 = trav(node.right)
            #return the max sum of current level, and next level
            return max(l1+r1, l2+r2+node.val), l1+r1
        return max(trav(root))
        
if __name__ == '__main__':
    s = Solution()
    print(s.rob([3,2,3,null,3,null,1]) == 7)