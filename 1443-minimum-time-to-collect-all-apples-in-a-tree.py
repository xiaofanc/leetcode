"""
The idea is to visit all the children of every node recursively, compute the time it takes to collect apples from each of the children, and use that time to compute the answer of the parent node.

1. Create a variable totalTime to store the time required to collect all the apples in the node's subtree. Initalize it with 0.
2. Iterate over all the children of the node (nodes that share an edge) and check if any child is equal to the parent. If the child is equal to the parent, we will not visit it again.
3. If the child is not equal to the parent, recursively call the dfs with node as child and parent as node. At the end of dfs traversal, we have the time required to collect all the apples in its subtree. Store it in childTime.
4. If the child has an apple (hasApple[child] = true) or there are any apples in its subtree, which can be checked if we need any time to collect apples (childTime > 0), we must visit child, which takes one unit of time, collect all apples in the child's subtree which takes childTime, and return, which again takes one unit of time. So, we add childTime + 2 to the totalTime.
5. If neither the child nor its subtree has apples, we don't need to include the time to visit this child, as we will consider we never visited this child's subtree.
"""

class Solution:
    # DFS
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, par):
            # time required to collect all the apples in the node's subtree
            totalTime = 0
            for nei in adj[i]:
                if nei == par:
                    continue
                # time required to collect the apples in the nei's subtree, not including nei
                childTime = dfs(nei, i)
                # check nei independently
                # if we have apple in the subtree or root, then we must visit current node nei and return it
                if childTime > 0 or hasApple[nei]:
                    totalTime += childTime + 2
            return totalTime
        
        return dfs(0, -1)

    # Topo sort
    # remove leaf edges without apple
    # res = (total edges - removed edges) * 2
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        degrees = [0]*n
        adj = defaultdict(set)

        for a, b in edges:
            degrees[a] += 1
            degrees[b] += 1
            adj[a].add(b)
            adj[b].add(a)

        removed = 0
        queue = deque([i for i in range(n) if degrees[i] == 1 and not hasApple[i]])
        while queue:
            node = queue.popleft()
            if node == 0:
                continue
            degrees[node] -= 1
            for nei in adj[node]:
                degrees[nei] -= 1
                adj[nei].remove(node)
                if degrees[nei] == 1 and not hasApple[nei]:
                    queue.append(nei)
                removed += 1
            del adj[node]
        return (len(edges)-removed)*2


