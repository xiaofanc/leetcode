"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
本质就是寻找分割点，分割点作为当前节点，然后递归左区间和右区间。
"""

from typing import List
class TreeNode:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return 
        mid = (len(nums)-1)//2 
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


if __name__ == '__main__':
	s=s = Solution()
	print(s.sortedArrayToBST([-10,-3,0,5,9]))