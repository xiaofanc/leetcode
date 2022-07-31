class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adjList = defaultdict(list)
        for i, n in enumerate(edges):
            if n != -1:
                adjList[i].append(n)
        n1 = adjList[node1][0]
        n2 = adjList[node2][0]
        if node1 == node2:
            return 0
        while n1 != n2:
            