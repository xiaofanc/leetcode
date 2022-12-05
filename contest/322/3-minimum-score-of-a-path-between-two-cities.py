class Solution:
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
            # print("q ->", q)
        return res
        
        
            
            