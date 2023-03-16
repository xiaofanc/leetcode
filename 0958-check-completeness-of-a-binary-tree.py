# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # left child: 2i+1, right child: 2i+2
        # if the index >= number of nodes, then it is not a complete tree
        def countNodes(node):
            return 1 + countNodes(node.left) + countNodes(node.right) if node else 0
        
        n = countNodes(root)

        def dfs(node, idx):
            if not node:
                return True
            if idx >= n:
                return False
            if not dfs(node.left, 2*idx+1) or not dfs(node.right, 2*idx+2):
                return False
            return True
        
        return dfs(root, 0)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # BFS
        queue = deque([root])
        nullFound = False
        while queue:
            node = queue.popleft()
            if not node:
                nullFound = True
            else:
                if nullFound:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # BFS
        queue = deque([root])
        prev = root
        while queue:
            node = queue.popleft()
            if node:
                if not prev:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            prev = node
        return True




        
            