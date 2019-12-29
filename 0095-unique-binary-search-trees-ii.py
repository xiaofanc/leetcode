# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            return [node(root, left, right) 
                   for root in range(first, last+1)
                   for left in trees(first, root-1)
                   for right in trees(root+1, last)] or [None]
        return trees(1,n)

if __name__ == '__main__':
  s = Solution()
  print(s.generateTrees(3))