"""
return the max path sum for a tree

  -10
  /  \
 9   20
    /  \
   -3   4  

What if we only have negative numbers?
What if we have -3 on the left?

"""
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def maxPathSum(root):
	res = float("-inf")

	def helper(node):
		nonlocal res
		# does not work when leaf node is the max path sum
		# a leaf node can be the path !!!!
		# if not node.left and not node.right:   
			# return node.val
		if not node:
			return 0
		# need the path sum from left subtree and right subtree
		# do not want to add negative num in the path
		leftSum = max(0, helper(node.left))  
		rightSum = max(0, helper(node.right))

		# calculate the max path sum in current level
		res = max(res, node.val + leftSum + rightSum)

		return max(leftSum, rightSum) + node.val

	helper(root)
	return res

T = TreeNode
root1 = T(-10, T(9), T(20, T(-3), T(4)))  # 24
print(maxPathSum(root1))
root2 = T(-10, T(-9), T(-12, T(-3), T(-1))) # -1
print(maxPathSum(root2))



