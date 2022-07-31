

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adjList = defaultdict(list)
        for i, n in enumerate(edges):
            if n != -1:
                adjList[i].append(n)
        # print("adjList", adjList)
        cnt = -1
        
        memo = {}
        def dfs(node, path, l):
            nonlocal cnt
            if node in memo:
                return memo[node]
            print("path", node, path)
            if node in visited:
                # print("path", path)
                cycle = path.index(node)
                cnt = max(cnt, l - cycle)
                memo[node] = cnt
                return
            path.append(node)
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei, path, l+1)
            # path.pop()
            # visited.remove(node)
        
        for node in range(len(edges)):
            visited = set()
            dfs(node, [], 0)
        return cnt
            
            