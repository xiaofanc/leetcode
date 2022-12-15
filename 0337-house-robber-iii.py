# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def trav(node):
            if not node: return (0, 0)
            #node.left level1 and level2
            l1, l2 = trav(node.left)
            #node.right level1 and level2
            r1, r2 = trav(node.right)
            #return the max sum of current level, and next level
            return max(l1+r1, l2+r2+node.val), l1+r1
        return max(trav(root))
        
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]
            rob_it = node.val
            if node.left:
                rob_it += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_it += dfs(node.right.left) + dfs(node.right.right)
            not_rob_it = dfs(node.left) + dfs(node.right)
            res = max(rob_it, not_rob_it)
            memo[node] = res
            return res
            
        return dfs(root)

if __name__ == '__main__':
    s = Solution()
    print(s.rob([3,2,3,null,3,null,1]) == 7)

