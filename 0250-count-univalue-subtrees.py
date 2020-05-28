# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return None
            lval = dfs(node.left)
            rval = dfs(node.right)
            is_unival = (lval == None or node.val == lval) and (rval == None or node.val == rval)
            if is_unival:
                self.ans += 1
                return node.val
            return "*" # 1 return * in the following example
        dfs(root)
        return self.ans
        
            
if __name__ == '__main__':
    s = Solution()
    print(s.countUnivalSubtrees([5,1,5,5,5,null,5]) == 4)