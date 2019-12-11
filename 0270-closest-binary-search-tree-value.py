class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        mindiff = float("inf")
        minv = float("inf")
        def inorder(root):
            if not root:return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        for i in inorder(root):
            if abs(i-target) < mindiff:
                mindiff = abs(i-target)
                minv = i
        
        return minv

    def closestValue(self, root: TreeNode, target: float) -> int:
        mindiff = float("inf")
        minv = float("inf")
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)
        
        for i in inorder(root):
            if abs(i-target) < mindiff:
                mindiff = abs(i-target)
                minv = i
        
        return minv


if __name__ == '__main__':
    T = TreeNode
    root = T(4, T(2, T(1), T(3)), T(5))
    s = Solution()
    print(s.closestValue(root, 3.71))

