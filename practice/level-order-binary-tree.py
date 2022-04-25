class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
"""
Question: return a list of list for a binary tree in level order
"""
class Solution:
	def levelOrder(self, root):
		level = [root]
		res = []
		while level:
			res.append([node.val for node in level])
			level = [child for node in level for child in [node.left, node.right] if child]
		return res

	# generator
	def levelOrder2(self, root):
		level = [root]
		while level:
			yield [node.val for node in level]
			level = [child for node in level for child in [node.left, node.right] if child]

if __name__ == '__main__':
	s = Solution()
	T = TreeNode
	root = T(1, T(2, T(4)), T(3, T(5, T(7)), T(6)))
	# print(s.levelOrder(root))
	g = s.levelOrder2(root)
	print(next(g))
	print(next(g))
	print(next(g))



	




		