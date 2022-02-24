"""
First call l, r to finish the traversal of a tree and used self.existp self.existq to check the two target nodes exsit in the tree.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.existp, self.existq = False, False
        
        def dfs(root, p, q):
            if not root: return root
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if root == p:
                self.existp = True
                return root
            if root == q:
                self.existq = True
                return root
            if l and r: # find both p and q
                return root
            return l or r
        
        ans = dfs(root, p, q)
        return ans if self.existp and self.existq else None

if __name__ == '__main__':
    s = Solution()
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,1))  # 3
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,4))  # 4
    print(s.lowestCommonAncestor([3,5,1,6,2,0,8,null,null,7,4],5,10)) # None 