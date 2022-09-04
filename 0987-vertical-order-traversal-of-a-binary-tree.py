# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        
        # Time: O(N)
        def dfs(node, row, col):
            if not node:
                return
            nodes[col].append((row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        res = []
        # sort by col
        # if same col, sort by row
        # if same row, sort by node.val
        # Time: O(ClogCxMlogM)
        for col, values in sorted(nodes.items()):
            temp = []
            for row, node in sorted(values):
                temp.append(node)
            res.append(temp)
        return res

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        minCol, maxCol = 0, 0
        def dfs(node, row, col):
            nonlocal minCol, maxCol
            if not node:
                return
            if col < minCol:
                minCol = col
            if col > maxCol:
                maxCol = col
            nodes[col].append((row, node.val))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        res = []
        
        # Time: O(Nlog(N/C))
        for col in range(minCol, maxCol+1):
            values = nodes[col]
            res.append([node for row, node in sorted(values)])
            # temp = []
            # for row, node in sorted(values):
            #     temp.append(node)
            # res.append(temp)
        return res
            
            
