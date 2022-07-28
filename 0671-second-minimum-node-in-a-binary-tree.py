# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # find the next value > root
        small = root.val
        res = [float('inf')]
        def preorder(node):
            if not node:
                return
            if small < node.val < res[0]:
                res[0] = node.val
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return -1 if res[0] == float("inf") else res[0]

if __name__ == '__main__':
    s = Solution()
    print(s.findSecondMinimumValue([2,2,5,null,null,5,7]))   # 5