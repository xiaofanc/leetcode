"""
首先要注意是判断左叶子，不是二叉树左侧节点.
因为题目中其实没有说清楚左叶子究竟是什么节点，那么我来给出左叶子的明确定义：如果左节点不为空，且左节点没有左右孩子，那么这个节点的左节点就是左叶子.

"""
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
	def sumOfLeftLeaves(self, root: TreeNode) -> int:
		if not root:
			return 0
		elif root.left and not any([root.left.left, root.left.right]):
			return root.left.val + self.sumOfLeftLeaves(root.right)
		else:
			# sum up the left leaves of left subtree and right subtree
			return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
		
		
	def sumOfLeftLeaves(self, root: TreeNode) -> int:
		"""
		1. we use a list to store nodes and res to store sum of left leaves
		2. for every node, check if it has left node and right node
		3. if it has left node, append it to the list and if it is a leaf, add to the res
		4. if it has right node, append it (a right node can have left leaf)
		"""
		if not root:
			return 0
		res = 0
		s = [root]
		while s:
			tmp = s.pop()
			if tmp.left:
				s.append(tmp.left)
				if not tmp.left.left and not tmp.left.right:
					res += tmp.left.val
			if tmp.right:
				s.append(tmp.right)
		return res

if __name__ == '__main__':
	T = TreeNode
	# root = T(1, T(2), T(3,T(4)))
	root2 = T(3, T(9), T(20, T(15, T(3), T(6)), T(7)))
	s = Solution()
	# print(s.sumOfLeftLeaves(root) == 6)
	print(s.sumOfLeftLeaves(root2) == 12)  # 9+3



