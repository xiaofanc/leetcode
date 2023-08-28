class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjlist = defaultdict(list)
        for i, m in enumerate(manager):
            adjlist[m].append(i)
        
        queue = deque()
        queue.append((headID, 0))
        res = 0
        
        while queue:
            node, total = queue.popleft()
            total += informTime[node]
            res = max(res, total)
            for nei in adjlist[node]:
                queue.append((nei,total))
        return res
                
        