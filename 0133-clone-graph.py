"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Time: O(V+E)
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def DFS(node):
            # if node has a copy
            if node in oldToNew:
                return oldToNew[node]
            # else
            copy = Node(node.val)
            oldToNew[node] = copy
            # add neighbors
            for nei in node.neighbors:
                copy.neighbors.append(DFS(nei))
            return copy
        return DFS(node) if node else None

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {node: Node(node.val)}

        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m: # <- this is the map used
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]

