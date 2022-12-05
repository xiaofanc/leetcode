"""
The number of group we can create for a connected graph is the maximum of minimum distances between all nodes in that graph. Here distance equals to number of nodes in the path.

If there is a odd-length cycle, it is impossible to divide the nodes, which is checked by the DFS part;
If it is possible, then we can enumerate all nodes via BFS to check for the largest number of division along each connected component, which is computed by the BFS part.
"""

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # find all connnected components in the graph - dfs
        # if a cycle with odd length is detected, return -1
        groups = []
        seen = [0]*(n+1)
        for i in range(1, n+1):
            if seen[i] == 0:
                groups.append([i])
                seen[i] = 1
                stack = [i]
                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if seen[v] == 0:
                            seen[v] = seen[u] + 1
                            stack.append(v)
                            groups[-1].append(v)
                        elif (seen[u] - seen[v]) % 2 == 0:
                            return -1

        # for each cc, find the max distance - BFS
        def bfs(i):
            q = deque()
            q.append((i, 1))
            visited = set()
            visited.add(i)
            while q:
                node, g = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        q.append((nei, g+1))
                        visited.add(nei)
            return g
        
        res = 0
        for i in range(len(groups)):
            res += max(bfs(j) for j in groups[i])
        return res


        

