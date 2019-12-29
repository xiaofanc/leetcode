class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node):
            if node == None: return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        def findswapped(nums):
            return [i for i,j in zip(nums, sorted(nums)) if i != j]
        def findnode(node, target):
            if node == None: return None
            if node.val == target: return node
            return findnode(node.left, target) or findnode(node.right, target)
        x, y  = findswapped(list(inorder(root)))
        nx,ny = findnode(root, x), findnode(root, y)
        nx.val, ny.val = ny.val, nx.val

if __name__ == '__main__':
    s = Solution()
    T = TreeNode
    t = T(1, T(3, None, T(2)))
    print(s.recoverTree(t))
    print(t)