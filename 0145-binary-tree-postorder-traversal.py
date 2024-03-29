"""
postorder: left + right + node

Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes, i.e. the size of tree.

Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # similar to preorder traversal - BFS
    # pop -> 中右左 -> reverse -> 左右中(postorder)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        res = res[::-1]
        return res

    # 统一写法 BFS
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            top = stack[-1]
            if top != None:
                node = stack.pop()
                stack.append(node)
                stack.append(None)
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
            else:
                stack.pop() # pop the None
                node = stack.pop()
                res.append(node.val)
        return res

    # DFS - recursion
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return  self.postorderTraversal(root.left) + self.postorderTraversal(root.right) +[root.val] if root else []

    # DFS - recursion
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            helper(cur.right)
            res.append(cur.val)
        helper(root)
        return res

