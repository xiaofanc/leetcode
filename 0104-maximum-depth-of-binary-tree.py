# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

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