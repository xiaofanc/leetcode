class Solution:
    # 64 / 73 passed
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        memo = {}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            memo[(a,b)] = 1
            memo[(b,a)] = 1

        def calculateDist(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if (j, i) in memo:
                return memo[(j, i)]
            q = deque()
            q.append((i, 0))
            visited = set()
            visited.add(i)
            while q:
                node, d = q.popleft()
                if node == j:
                    return d
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        memo[(i, nei)] = d+1
                        memo[(nei, i)] = d+1
                        q.append((nei, d+1))
            return 0
                
        res = []
        for i in range(n):
            d = 0
            for j in range(n):
                if i != j:
                    d += calculateDist(i, j)
            res.append(d)
        return res

"""
Let's investigate the answers of neighboring nodes x and y.
In particular, say xyxyxy is an edge of the graph, that if cut would form two trees X (containing x) and Y (containing y).
Answer for x in the entire tree:
answer of x on X "x@X" + (the answer of y on Y "y@Y" + number of nodes in Y "#(Y)"
since dist(x, z) = dist(y, z) + 1, where z on Y.

By similar reasoning, the answer for y in the entire tree is ans[y] = x@X + y@Y + #(X). Hence, for neighboring nodes x and y, ans[x] - ans[y] = #(Y) - #(X)

step 1: post-order traversal calculate: 
count[node] += count[child] and stsum[node] += stsum[child] + count[child]
This will give us the right answer for the root: ans[root] = stsum[root]

step 2: update res for each node
if we have a node parent and it's child, then these are neighboring nodes, split child and parant, so we have
ans[child] = ans[parent] - count[child] + (N - count[child])
Using a second, pre-order traversal, we can update our answer in linear time for all of our nodes.
"""
                
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        memo = {}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            memo[(a,b)] = 1
            memo[(b,a)] = 1

        res = [0]*n
        count = [1]*n

        def postorder(node=0, parent=None):
            # update count and subtree sum for the current node assuming child and parent is disconnected
            # res[0] is the correct final res since it does not have root
            for child in adj[node]:
                if child != parent:
                    postorder(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def preorder(node=0, parent=None):
            # update res for each node from top to down using res[0]
            for child in adj[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    preorder(child, node)

        postorder()
        preorder()
        return res
            
            
                
