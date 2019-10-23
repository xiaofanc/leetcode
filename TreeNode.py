class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


if __name__ == '__main__':
	T = TreeNode
	root = T(1, T(2), T(3,T(4)))
	print(root)