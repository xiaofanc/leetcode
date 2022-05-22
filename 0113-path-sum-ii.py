
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        def traversal(node, path, target):
            if not node.left and not node.right and target == 0:
                paths.append(path[:])
            if node.left:
                path.append(node.left.val)
                traversal(node.left, path, target-node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                traversal(node.right, path, target-node.right.val)
                path.pop()
        traversal(root, [root.val], targetSum-root.val)
        return paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        path = []
        def traversal(node, target):
            path.append(node.val)
            if not node.left and not node.right and target == node.val:
                paths.append(path[:])
            if node.left:
                traversal(node.left, target-node.val)
                path.pop()
            if node.right:
                traversal(node.right, target-node.val)
                path.pop()
        traversal(root, targetSum)
        return paths


