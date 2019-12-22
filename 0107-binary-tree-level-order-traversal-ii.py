from typing import List
from collections import defaultdict

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            ans.append([l.val for l in level])
            level = [child for n in level for child in (n.left, n.right) if child != None]
        return ans[::-1]

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        levels = defaultdict(list)
        if not root:
            return []
        def traverse(root, level):
            levels[level].append(root.val)
            if root.left:  traverse(root.left, level+1)
            if root.right: traverse(root.right, level+1)
        traverse(root, 0)
        print(levels)
        return [levels[i] for i in reversed(sorted(levels.keys()))]

if __name__ == '__main__':
	T = TreeNode
	root = T(1, T(2), T(3,T(4)))
	s = Solution()
	print(s.levelOrderBottom(root))
	print(root)