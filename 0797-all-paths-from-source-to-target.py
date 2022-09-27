class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def dfs(node, path):
            if node == n-1:
                res.append(path[:])
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        
        dfs(0, [0])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[1,2],[3],[3],[]])) # [[0,1,3],[0,2,3]]