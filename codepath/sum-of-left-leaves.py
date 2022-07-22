class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
	def sumOfLeftLeaves(self, root: TreeNode):
		def helper(root, sumSoFar):
			if not root:
				return sumSoFar
			if root.left:
				sumSoFar += root.left.val
			return helper(root.left, sumSoFar) + helper(root.right, sumSoFar)
		return helper(root, 0)

if __name__ == '__main__':
	s = Solution()
	T = TreeNode
	root = T(3, T(9), T(20,T(15),T(7)))
	print(s.sumOfLeftLeaves(root))

		