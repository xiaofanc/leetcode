class Solution:
    # Topo sort
    # Start from nodes with indegree = 0
    # Keep track of the maximum freq of all the colors for paths that end at node x
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # u -> v, use the maximum frequencies of colours across all paths that end with u to form the maximum frequencies of colours for paths that end with v
        adj = defaultdict(list)
        n = len(colors)
        indegree = [0]*n
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1
        
        # keeps track of the maximum frequencies of all the colors for paths that end at node x
        count = [[0 for j in range(26)] for i in range(n)]

        res = 0
        seen = 0
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            color = ord(colors[node]) - ord('a')
            # get the final count for the node (indegree[i] == 0)
            count[node][color] += 1
            res = max(res, count[node][color])
            seen += 1
            for nei in adj[node]:
                for i in range(26):
                    # update the count for the children
                    count[nei][i] = max(count[nei][i], count[node][i])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        if seen < n:
            return -1
        return res

class Solution:
    # TLE...max freq of color for paths that starts with node is repeatly calculated
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
        
        res = -1
        def dfs(i, d):
            nonlocal res
            # print(" "*d, i)
            if i in visited:
                return True # cycle
            visited.add(i)
            path[colors[i]] += 1
            nodes.add(i)
            # print("     "*d, path)
            if path[colors[i]] > res:
                res = path[colors[i]]
            for nei in adj[i]:
                if dfs(nei, d+1):
                    return True
            visited.remove(i)
            path[colors[i]] -= 1
            return False

        n = len(colors)
        nodes = set()
        for i in range(n):
            if i not in nodes:
                # print("visiting...")
                visited = set()
                path = defaultdict(int)
                if dfs(i, 0):
                    return -1
        return res



