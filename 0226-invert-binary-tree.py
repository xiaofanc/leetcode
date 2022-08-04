# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time: O(N)
class Solution:
    # DFS
    # Time: O(N)
    # Space: O(N) for unbalanced tree, O(logN) for balanced tree
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # preorder traversal - DFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        def helper(node):
            if not node:
                return
            else:
                node.left, node.right = node.right, node.left
            if node.left: helper(node.left)
            if node.right: helper(node.right)
        helper(root)
        return root

    # DFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right = node.right, node.left
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return root

    # BFS 广度优先搜索
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        level = [root]
        while level:
            for node in level:
                node.left, node.right = node.right, node.left
            level = [c for node in level for c in (node.left, node.right) if c]
        return root

    # BFS
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft() # level order
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

if __name__ == '__main__':
    s = Solution()
    print(s.invertTree([4,2,7,1,3,6,9]))

