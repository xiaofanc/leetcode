"""
2385.
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        edges = defaultdict(list)
        def createEdges(root):
            if not root:
                return 
            if root.left: 
                edges[root.val].append(root.left.val)
                edges[root.left.val].append(root.val)
            if root.right:
                edges[root.val].append(root.right.val)
                edges[root.right.val].append(root.val)
            createEdges(root.left)
            createEdges(root.right)
        createEdges(root)
        
        # print("edges->", edges)
        visited = set()
        visited.add(start)
        # use BFS to infect the neighbors
        queue = deque()
        queue.append((start, 0))
        while queue:
            node, depth = queue.popleft()
            for nei in edges[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, depth+1))
        return depth
                
                
            
            