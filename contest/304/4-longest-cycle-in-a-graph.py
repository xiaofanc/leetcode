

class Solution:
	# TLE
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

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def dfs(node, path, l):
            nonlocal maxl
            # print("path", node, path, l)
            if node == -1:
                return
            if node in visited:
                # check if node in the path
                idx = -1
                for i, n in enumerate(path):
                    if n == node:
                        idx = i
                if idx == -1:
                    return
                else:
                    maxl = max(maxl, l-idx)
                    # print("l, idx, maxl", l, idx, maxl)
                    return
            visited.add(node)
            path.append(node)
            dfs(edges[node], path, l+1)
                
        maxl = -1
        visited = set()
        for node in range(len(edges)):
            dfs(node, [], 0)
        return maxl
            

    def longestCycle(self, edges: List[int]) -> int:
        # Time: O(N)
        # cycle will be visited once
        # each node will be visited once
        def dfs(node, idx, path, l):
            nonlocal maxl
            if node == -1: # no cycle
                return
            if node in visited:
                # get the index of node if it is in the path
                i = idx.get(node, -1)
                # node is not in the path, but visited in previous path
                # no need to continue
                if i == -1:
                    return
                else:
                    maxl = max(maxl, l-i)
                    return
            idx[node] = l
            visited.add(node)
            path.append(node)
            dfs(edges[node], idx, path, l+1)
                
        maxl = -1
        visited = set()           # global
        for node in range(len(edges)):
            idx = defaultdict()   # local
            dfs(node, idx, [], 0)
        return maxl
            

