class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def helper(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return helper(root1.left, root2.left) and helper(root1.right, root2.right)
            else:
                return False
        
        return helper(p, q)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: # p == None
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == '__main__':
    T = TreeNode
    p = T(1, T(2), T(3,T(4)))
    q = T(1, T(2), T(3,None,T(4)))
    s = Solution()
    print(s.isSameTree(p, q))

