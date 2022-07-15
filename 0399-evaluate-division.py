class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        dct = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            dct[a].append((b, values[i]))
            dct[b].append((a, 1/values[i]))

        def dfs(node, target, prod):
            if node in visited:
                return
            if node == target:
                res.append(prod)
                return True
            visited.add(node)
            if node not in dct:
                return False
            for nei, edge in dct[node]:
                prod *= edge
                if dfs(nei, target, prod): return True
                prod /= edge
            return False

        res = []
        for c, d in queries:
            visited = set()
            if c == d and c in dct:
                res.append(1)
                continue
            elif c == d or c not in dct:
                res.append(-1)
                continue
            exists = dfs(c, d, 1)
            if not exists: res.append(-1)
        return res

if __name__ == '__main__':
    s = Solution()
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(s.calcEquation(equations, values, queries))


