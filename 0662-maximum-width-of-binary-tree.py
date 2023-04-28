# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	# 72 / 114 testcases passed
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = [root]
        res = 0
        while level:
            temp = []
            l, r = -1, -1
            for i, node in enumerate(level):
                if node != None:
                    if l == -1:
                        l = i
                        r = i  # [1]
                    else:
                        r = i
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    temp.append(None)
                    temp.append(None)
            if l == -1:  # no node 
                break
            level = temp
            res = max(res, r-l+1)
        return res

    # create index for each node
    # BFS
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = [(root, 0)]
        res = 0
        while level:
            temp = []
            res = max(res, level[-1][1]-level[0][1]+1)
            for node in level:
                node, idx = node[0], node[1]
                if node.left:
                    temp.append((node.left, 2*idx))
                if node.right:
                    temp.append((node.right, 2*idx+1))
            level = temp
        return res

    # DFS: store index for each level
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tree = []
        def dfs(node, i, depth):
            if not node:
                return
            if len(tree) == depth:
                tree.append([])
            tree[depth].append(i)
            dfs(node.left, 2*i, depth+1)
            dfs(node.right, 2*i+1, depth+1)
        dfs(root, 0, 0)
        res = 0
        for level in tree:
            res = max(res, level[-1]-level[0]+1)
        return res

    # DFS - only store the first index of each level
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        first_idx = {}
        res = 0
        def dfs(node, i, depth):
            nonlocal res
            if not node:
                return
            if len(first_idx) == depth:
                first_idx[depth] = i
            res = max(res, i-first_idx[depth]+1)
            dfs(node.left, 2*i, depth+1)
            dfs(node.right, 2*i+1, depth+1)
        dfs(root, 0, 0)
        return res



