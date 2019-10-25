class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    # DFS
    def isSubtree0(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        if self.ismatch(s, t): return True
        return self.isSubtree0(s.left, t) or self.isSubtree0(s.right, t)
    
    def ismatch(self, s, t):
        if not (s and t):
            return s is t
        return s == t and self.ismatch(s.left, t.left) and self.ismatch(s.right, t.right)

    # convert to string
    def isSubtree1(self, s: TreeNode, t: TreeNode) -> bool:
        def convert(p):
            return '^' + str(p.val) + '#' + convert(p.left) + convert(p.right) if p else '$'   
        return convert(t) in convert(s)
        
if __name__ == '__main__':
    T = TreeNode
    s = T(1, T(2,T(3),T(4)), T(2,T(4),T(3)))
    t = T(2,T(4),T(3))
    print(t, s)

s = Solution()

print(s.isSubtree0(s, t))
print(s.isSubtree1(s, t))