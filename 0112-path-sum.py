class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
	# recursion
    # Time: O(n), space: O(h), h = logn for balanced tree, h = n for unbalanced tree
    def hasPathSum(self, root: TreeNode, sum: int) :
        if not root:
            return
        sum -= root.val
        if not root.left and not root.right: # reach the bottom
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root and not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def traversal(node, target):
            if not node.left and not node.right and target == 0:
                return True
            if node.left:
                if traversal(node.left, target-node.left.val):
                    return True
            if node.right:
                if traversal(node.right, target-node.right.val):
                    return True
        if traversal(root, targetSum-root.val):
            return True
        return False

    # iteration
    def hasPathSum(self, root: TreeNode, sum: int) :
        if not root:
            return False
        cur = [(root, sum - root.val),]
        while cur:
            node, curr_sum = cur.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                cur.append((node.left, curr_sum - node.left.val))
            if node.right:
                cur.append((node.right, curr_sum - node.right.val))
        return False
        
    # does not work in cases! path must from root to leaf node!
    #   1
    #  2
    # 3
    #  4
    # target = 6 will return True in this case since 3 does not have left child
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return target == 0
        return self.hasPathSum(root.left, target-root.val) or self.hasPathSum(root.right, target-root.val)

if __name__ == '__main__':
	T = TreeNode
	root = T(5, T(4, T(11, T(7), T(2)), None), T(8,T(13),T(4, None, T(1))))
	print(root)

	s = Solution()
	print(s.hasPathSum(root, 22))
    print(s.hasPathSum(T(None), 0))  # False


    
