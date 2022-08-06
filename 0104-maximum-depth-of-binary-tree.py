# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # DFS
    # Time: O(N)
    # Space: O(N) for unbalanced tree, O(logN) for balanced tree
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 # this is height
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0  # this is depth
        res = 0
        def dfs(node):
            nonlocal depth, res
            if not node:
                return
            depth += 1
            res = max(res, depth)
            dfs(node.left)
            dfs(node.right)
            depth -= 1
        dfs(root)
        return res

    # iterative DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [[root,1]]
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res

    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = [root]
        depth = 0
        while level:
            depth += 1
            level = [c for node in level for c in (node.left, node.right) if c]
        return depth

    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = deque([(root, 1)])
        depth = 0
        while level:
            node, depth = level.popleft()
            if node.left: level.append((node.left, depth+1))
            if node.right: level.append((node.right, depth+1))
        return depth



        