# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)  # node + left + right
            if node.right: stack.append(node.right)
            if node.left:  stack.append(node.left)
        return ans
                
            
if __name__ == '__main__':
    s = Solution()
    print(s.preorderTraversal([1,null,2,3]) == [1,2,3])