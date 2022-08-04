# Definition for a binary tree node.
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(n), call stack may take O(H) space
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.maxnode = root.val
        
        # maxnode is the maximum for the current path - not global maximum
        def tranverse(root, maxnode):
            if not root:
                return
            maxnode = max(maxnode, root.val)
            if root.left and maxnode <= root.left.val:
                self.ans += 1
            if root.right and maxnode <= root.right.val:
                self.ans += 1
                
            tranverse(root.left, maxnode)
            tranverse(root.right, maxnode)
            
        tranverse(root, self.maxnode)
        return self.ans+1  # root is always good


    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.maxnode = root.val
        
        def tranverse(node, maxnode):
            if not root:
                return
            if maxnode <= node.val:
                self.ans += 1
            if node.left:
                tranverse(node.left, max(maxnode, node.val))
            if node.right:
                tranverse(node.right, max(maxnode, node.val))
            
        tranverse(root, self.maxnode)
        return self.ans

    # top-down DFS
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, maxVal):
            nonlocal cnt
            if not node:
                return 0
            if node.val >= maxVal:
                cnt += 1
                maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, float('-inf'))
        return cnt

    # top-down DFS
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        res = 0
        while stack:
            node, maxVal = stack.pop()
            if node.val >= maxVal:
                res += 1
                maxVal = node.val
            if node.left: stack.append((node.left, maxVal))
            if node.right: stack.append((node.right, maxVal))
        return res

if __name__ == '__main__':
    T = TreeNode
    root = T(3, T(1, T(3)), T(4,T(1), T(5)))
    s = Solution()
    print(s.goodNodes(root))  # 4

