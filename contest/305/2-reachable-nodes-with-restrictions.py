"""
6139.
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.
"""

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adjList = defaultdict(list)
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        
        rest = set(restricted)
        visited = set()
        def dfs(node, prev):
            if node in visited or node in rest:
                return
            visited.add(node)
            for nei in adjList[node]:
                if nei != prev:
                    dfs(nei, node)
        dfs(0, -1)
        return len(visited)

