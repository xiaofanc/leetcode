# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def balance(root):
            if not root:
                return 0
            l = balance(root.left)
            r = balance(root.right)
            self.ans += abs(l) + abs(r) # total movement in that subtree
            return root.val - 1 + l + r # total balance of subtree
        balance(root)
        return self.ans

if __name__ == '__main__':
    s = Solution()
    print(s.distributeCoins([1,0,0,null,3]) == 4)