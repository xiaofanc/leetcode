class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dct = defaultdict(set)
        notequal = defaultdict(set)
        for equation in equations:
            a, b = equation[0], equation[3]
            if equation[1:3] == "==":
                if a == b:
                    continue
                else:
                    dct[a].add(b)
                    dct[b].add(a)
            else:
                if a == b:
                    return False
                else:
                    notequal[a].add(b)
                    notequal[b].add(a)
        
        def dfs(node, target, visited):
            if node == target:
                return False
            if node in visited:
                return True
            visited.add(node)
            for nei in dct[node]:
                if not dfs(nei, target, visited):
                    return False
            visited.remove(node)
            return True
        
        for k, values in notequal.items():
            for v in values:
                visited = set()
                if not dfs(k, v, visited):
                    return False
        return True
    
    # Time: O(N)
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = [[] for i in range(26)]
        for equa in equations:
            if equa[1] == "=":
                x = ord(equa[0]) - ord('a')
                y = ord(equa[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)
        
        def dfs(node, c):
            if color[node] == -1:
                color[node] = c
                for nei in graph[node]:
                    dfs(nei, c)
            
        # mark the connected component same color
        color = [-1] * 26
        for i in range(26):
            if color[i] == -1:
                dfs(i, i)
        
        for equa in equations:
            if equa[1] == "!":
                x = ord(equa[0]) - ord('a')
                y = ord(equa[3]) - ord('a')
                if color[x] == color[y]:
                    return False
        return True

    # Union-find time: O(Nlog26)
    def equationsPossible(self, equations: List[str]) -> bool:
        root = [i for i in range(26)]
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            r1, r2 = find(x), find(y)
            root[r1] = r2
        
        for eqn in equations:
            if eqn[1] == "=":
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                union(x, y)
                # print("union->", root)
        
        for eqn in equations:
            if eqn[1] == "!":
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                if find(x) == find(y):  # if root is same
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.equationsPossible(["b==b","b==e","e==c","d!=e"])) # True
    print(s.equationsPossible(["a==b","b==e","e==c","a!=c"])) # False



            
                