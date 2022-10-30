# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TLE: 30/39
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        def getHeight(node):
            if not node:
                return -1
            l = getHeight(node.left)
            r = getHeight(node.right)
            return max(l, r) + 1
        
        def removeNode(node, val):
            if not node or node.val == val:
                return None
            node.left = removeNode(node.left, val)
            node.right = removeNode(node.right, val)
            return node
        
        def copyTree(root):
            if not root:
                return None
            node = TreeNode(root.val)
            node.left = copyTree(root.left)
            node.right = copyTree(root.right)
            return node
        
        res = [0]*len(queries)
        for i, q in enumerate(queries):
            newTree = copyTree(root)
            newRoot = removeNode(newTree, q)
            height = getHeight(newRoot)
            res[i] = height
        return res


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # each node has a depth and a height
        # length(heigth) of path = depth + height (node in the path)
        # after removing the node, find the cousins (same depth) with the largest height
        depth, height = defaultdict(int), defaultdict(int)
        
        # find the depth and height for each node
        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            h = max(dfs(node.left, d+1), dfs(node.right, d+1)) + 1
            height[node.val] = h
            return h
        
        dfs(root, 0)
        # keep top 2 largest height for same depth
        # depth: (height, node.val)
        cousins = defaultdict(list)
        for node, d in depth.items():
            cousins[d].append((-height[node], node))
            cousins[d].sort()
            if len(cousins[d]) > 2:
                cousins[d].pop()
        
        res = []
        for q in queries:
            d = depth[q]
            # find the cousin with the largest height
            # if the node removed has the largest height
            if q == cousins[d][0][1]:
                # only one node on this level
                if len(cousins[d]) == 1:
                    res.append(d-1)
                else:
                    res.append(-cousins[d][1][0]+d)
            # if other node has the largest height
            else:
                res.append(-cousins[d][0][0]+d)
        return res
                    
            
        
        

            