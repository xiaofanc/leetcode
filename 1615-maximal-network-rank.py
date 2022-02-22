from collections import defaultdict

class Solution:
    # Time: O(n^2), Space: O(E)
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(list)
        for node1, node2 in roads:
            edges[node1].append(node2)
            edges[node2].append(node1)
        # print(edges)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, len(edges[i])+len(edges[j])-(i in edges[j]))
        return res

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(dict)
        for a, b in roads:
            d[a][b] = d[b][a] = 1
        
        return max(len(d[a]) + len(d[b]) - (a in d[b]) for a, b in combinations(range(n), 2))
        
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edges = [0] * n
        roadslookup = set()
        for node1, node2 in roads:
            edges[node1] += 1
            edges[node2] += 1
            roadslookup.add((node1, node2))
        ordering = [i for i in range(n)]
        # sort the node by number of edges for the early stop
        ordering.sort(key = lambda x: edges[x], reverse = True)
        # print(ordering) 
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                a = ordering[i]
                b = ordering[j]
                score = edges[a] + edges[b]
                if score < ans:
                    return ans # early stop
                if (a, b) in roadslookup or (b, a) in roadslookup:
                    score -= 1
                # print(edge_ab)
                ans = max(ans, score)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]))
    print(s.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))



