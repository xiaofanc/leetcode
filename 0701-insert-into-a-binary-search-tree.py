"""
只要遍历二叉搜索树，找到空节点插入元素就可以了，那么这道题其实就简单了。
终止条件就是找到遍历的节点为null的时候，就是要插入节点的位置了，并把插入的节点返回。
这里把添加的节点返回给上一层，就完成了父子节点的赋值操作了。
"""

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def insertIntoBST(self, root, val):
        if not root: # 找到遍历的节点为None
            node = TreeNode(val)
            return node
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        cur, parent = root, root
        # find the None position to insert
        # keep track of the parent
        while cur:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        if parent.val > val:
            parent.left = node
        else:
            parent.right = node
        return root

if __name__ == '__main__':
	s = Solution()
	T = TreeNode
	root = T(4, T(2, T(1), T(3)), T(7))
	print(s.insertIntoBST(root, 5))


