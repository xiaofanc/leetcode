class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def trans(root):
            if not root:
                return []
            return trans(root.left) + [root.val] + trans(root.right)
        
        tree = trans(root)
        return len(set(tree)) == 1

    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = (not root.left or (root.val == root.left.val and self.isUnivalTree(root.left)))
        right_correct = (not root.right or (root.val == root.right.val and self.isUnivalTree(root.right)))
        return left_correct and right_correct

    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            if root.val != root.left.val:
                return False
        if root.right:
            if root.val != root.right.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        def trans(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return trans(node.left, val) and trans(node.right, val)
        return trans(root, root.val)



if __name__ == '__main__':
	T = TreeNode
	root = T(5, T(5), T(5,T(5)))
	s = Solution()
	print(s.isUnivalTree(root))




