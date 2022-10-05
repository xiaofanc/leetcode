# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        q = deque()
        q.append((root, 1))
        while q:
            node, d = q.popleft()
            if d == depth-1:
                left, right = node.left, node.right
                node.left, node.right = TreeNode(val), TreeNode(val)
                node.left.left = left
                node.right.right = right
            if node.left: q.append((node.left, d+1))
            if node.right: q.append((node.right, d+1))
        return root
                
            