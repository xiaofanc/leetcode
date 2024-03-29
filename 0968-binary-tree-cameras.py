# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        covered = {None}
        
        def dfs(node, par = None):
            if node: 
                dfs(node.left, node)
                dfs(node.right, node)
                
                if (par is None and node not in covered or node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})
                    # print(covered)
        
        dfs(root)
        return self.ans

if __name__ == '__main__':
    T = TreeNode
    t1 = T(0, T(0, T(0, 0)))
    s = Solution()
    print(s.minCameraCover(t1)) #1