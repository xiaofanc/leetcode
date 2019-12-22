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
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
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
	root = T(1, T(2), T(3,T(4)))
	s = Solution()
	print(s.sumOfLeftLeaves(root) == 6)