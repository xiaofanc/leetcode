class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def diameterOfBinaryTree0(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1
        
        depth(root)
        return self.ans - 1


    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        
        depth(root)
        return self.ans 


if __name__ == '__main__':
    T = TreeNode
    t1 = T(1, T(2,T(4),T(5)), T(3))
    print(t1)

    s=Solution()
    print(s.diameterOfBinaryTree0(t1))
    print(s.diameterOfBinaryTree1(t1))