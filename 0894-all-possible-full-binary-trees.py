from typing import List

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'N(%s, %s, %s)' % (self.val, self.left or '', self.right or '')


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 0: return []
        if N == 1: return [TreeNode(0)]
        def TreenodeLR(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        # i 取值1，N-2 因为左边或右边一定要有值
        # L 取值所有可能的左子树
        # R 取值所有可能的右子树
        return [TreenodeLR(0, l, r) for i in range(1, N-1) for l in self.allPossibleFBT(i) for r in self.allPossibleFBT(N-i-1)]

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def TreenodeLR(val, left=None, right=None):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        memo = {0:[], 1:[TreeNode(0)]}
        def t(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = [TreenodeLR(0, l, r) for i in range(1, n-1) for l in t(i) for r in t(n-i-1)]
                return memo[n]
        return t(N)

if __name__ == '__main__':
    s = Solution()
    for t in s.allPossibleFBT(7): print(t)