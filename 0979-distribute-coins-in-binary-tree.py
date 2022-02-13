"""
Root asks the left subtree, how much do you need or you've got extra? I'll give that/take it away to/from you via our direct edge, and pass it to right child, and if something remains, I'll take it.
Same question is asked to the right child.
Answer will be the sum of values(absolute) returned after the asked questions from the left(Left) and right(Right).
But what should the root return to its parent? It will return that how much does "his tree" need/has extra. That will be the signed sum of its Left+Right (question's answer) + current.val - 1.

We traverse childs first (post-order traversal), and return the ballance of coins. For example, if we get '+3' from the left child, that means that the left subtree has 3 extra coins to move out. If we get '-1' from the right child, we need to move 1 coin in. So, we increase the number of moves by 4 (3 moves out left + 1 moves in right). We then return the final balance: r->val (coins in the root) + 3 (left) + (-1) (right) - 1 (keep one coin for the root).

https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n)
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def balance(root):
            if not root:
                return 0
            l = balance(root.left)
            r = balance(root.right)
            self.ans += abs(l) + abs(r) # total movement in that subtree
            return root.val - 1 + l + r # total excess of subtree
        balance(root)
        return self.ans

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves= 0
    
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # coins need to be moved/added to the left and right
            self.moves += abs(left) + abs(right)
            # for the current node, the excess coin it has now
            return root.val + left + right - 1
        
        dfs(root)
        
        return self.moves

if __name__ == '__main__':
    T = TreeNode
    root = T(1, T(0), T(0,T(3)))
    s = Solution()
    print(s.distributeCoins(root) == 4)


