class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True
        return abs(height(root.left)-height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node):
            if node == None:
                return (0, True)
            l_depth, l_balanced = check(node.left)
            r_depth, r_balanced = check(node.right)
            return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth-r_depth) < 2
        
        return check(root)[1]

if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(2), T(3,T(4)))
    s = Solution()
    print(s.isBalanced(root))
