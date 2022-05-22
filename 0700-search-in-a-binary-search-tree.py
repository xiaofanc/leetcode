class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "N(%s, %s, %s)" % (self.val, self.left or '', self.right or '')


class Solution:
    def searchBST(self, root: TreeNode, val: int):
        if not root:
            return
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        return root

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val > val:
                root = root.left
            elif root.val < val:
                root = root.right
            else:
                return root
        return root

if __name__ == '__main__':
    s = Solution()
    N = TreeNode
    t = N(4, N(2, N(1), N(3)), N(7))
    print(t)
    print(s.searchBST(t, 2))


    
