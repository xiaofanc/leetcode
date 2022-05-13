# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        res = []
        while level:
            res.append(max([node.val for node in level]))
            level = [c for node in level for c in (node.left, node.right) if c]
        return res

    # DFS - recursion
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def helper(node, depth):
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                helper(node.left, depth+1)
            if node.right:
                helper(node.right, depth+1)
        helper(root, 0)
        res = [max(l) for l in res]
        return res





        