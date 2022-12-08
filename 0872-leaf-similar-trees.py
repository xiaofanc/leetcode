# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def level(node, roots):
            if not node:
                return
            if not node.left and not node.right:
                roots.append(node.val)
            level(node.left, roots)
            level(node.right, roots)
            return roots
        l = level(root1, [])
        r = level(root2, [])
        p1, p2 = 0, 0
        while p1 < len(l) and p2 < len(r):
            if l[p1] != r[p2]:
                return False
            else:
                p1 += 1
                p2 += 1
        return p1 == len(l) and p2 == len(r)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def level(node):
            leaves = []
            if not node:
                return []
            if not node.left and not node.right:
                leaves.append(node.val)
            leaves += level(node.left)
            leaves += level(node.right)
            return leaves
        return level(root1) == level(root2)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        
        return list(dfs(root1)) == list(dfs(root2))


