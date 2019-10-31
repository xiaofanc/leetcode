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