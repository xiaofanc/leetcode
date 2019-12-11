class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.numofPaths = 0
        self.dfs(root, target)
        return self.numofPaths
    
    def dfs(self, node, target):
        if not node:
            return
        # check if path from node can sum up to target
        self.test(node, target)  
        # check if path from left node can sum up to target
        self.dfs(node.left, target) 
        # check if path from right node can sum up to target
        self.dfs(node.right, target)
        
    def test(self, node, target):
        if not node:
            return 
        if node.val == target:
            self.numofPaths += 1
        
        # test going downward
        self.test(node.left, target-node.val) 
        self.test(node.right, target-node.val)

if __name__ == '__main__':
    s = Solution()
    T = TreeNode
    t1 = T(10, T(5, T(3, T(3), T(-2)), T(2, None, T(1))), T(-3, None, T(11)))
    print(s.pathSum(t1, 8))
            