class Solution:
    # Find the min path connected 1 and n:
    # Every path connected to 1 can be visited
    # There is at least one path between 1 and n
    # The min score is the min path connected to 1
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        mind = float('inf')
        for a, b, d in roads:
            adj[a].append((b,d))
            adj[b].append((a,d))
            mind = min(mind, d)

        # we do not want to visit a path twice
        visited = set()
        res = float('inf')

        def dfs(i, d):
            nonlocal res
            if (i, d) in visited:
                return False
            if res == mind:
                return True
            if d < res:
                res = d
            visited.add((i, d))
            for nei in adj[i]:
                if dfs(nei[0], nei[1]):
                    return True
        dfs(1, float('inf'))
        return res

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dct = defaultdict(list)
        mind = float("inf")
        for a, b, d in roads:
            dct[a].append((b, d))
            dct[b].append((a, d))
            mind = min(mind, d)
        
        res = float("inf")
        # 找到路径经过的node连接的所有路的最小值
        q = deque()
        q.append((1, float("inf")))
        visited = set()
        while q:
            city, d = q.popleft()
            if (city, d) in visited:
                continue
            visited.add((city, d))
            if d < res:
                res = d
            if res == mind:
                return res
            for nei in dct[city]:
                q.append((nei[0], nei[1]))
        return res






