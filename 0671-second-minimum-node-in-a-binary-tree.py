# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # find the next value > root, could be in the deep 
        small = root.val
        res = [float('inf')]
        def preorder(node):
            if not node:
                return
            if small < node.val < res[0]:
                res[0] = node.val
                return              # 在左子树中找到值后return，继续查找右子树
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return -1 if res[0] == float("inf") else res[0]

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        smallest = root.val
        second = None
        def dfs(node):
            nonlocal smallest, second
            if not node:
                return 
            # go deeper only if node.val == smallest
            if node.val == smallest:
                dfs(node.left)
                dfs(node.right)
            else:
                if not second:
                    second = node.val
                else:
                    second = min(second, node.val)
        dfs(root)
        return -1 if not second else second

if __name__ == '__main__':
    s = Solution()
    print(s.findSecondMinimumValue([2,2,5,null,null,5,7]))   # 5
    print(s.findSecondMinimumValue([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]))   # 2





    
