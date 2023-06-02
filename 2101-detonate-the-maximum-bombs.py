class Solution:
    # Time: there are at most n nodes and n^2 edges = O(n^3)
    # Space: O(n^2)
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # create a directed graph
        adjlist = defaultdict(list) # which nodes that key can reach
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                b1, b2 = bombs[i], bombs[j]
                if (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 <= b1[2]**2:
                    adjlist[i].append(j)
                if (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 <= b2[2]**2:
                    adjlist[j].append(i)
        res = float('-inf')
        def dfs(i):
            nonlocal res, count
            visited.add(i)
            count += 1
            res = max(res, count)
            for nei in adjlist[i]:
                if nei not in visited:
                    dfs(nei)
        
        for i, bomb in enumerate(bombs):
            # get the max nodes that a node can reach
            visited = set()
            count = 0
            dfs(i)
        return res
                    
                
            