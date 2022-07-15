class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
	def printNodes(root):
		res = []
		def dfs(node):
			if not node:
				return 0
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if not node.left and not node.right:
				res.append(node.val)
			return None

		dfs(root)
		# return res

		depthMap = {}
		def depth(root):
			if not root:
				depthMap[root] = 0
				return 0
			if root in depthMap:
				return depthMap[root]
			leftDepth = depth(root.left)
			rightDepth = depth(root.right)
			depthMap[root] = min(leftDepth, rightDepth)+1
			return depthMap[root]
		depth(root)
		print("depth", depthMap)


if __name__ == '__main__':
	T = TreeNode
	root = T(1, T(2), T(3,T(4)))
	# print(root)
	s = Solution
	print(s.printNodes(root))