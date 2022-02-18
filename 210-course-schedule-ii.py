from collections import defaultdict

# solution 1: DFS, Time: O(V+E), space: O(V+E)
class Solution:
    white = 1
    gray = 2
    black = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        topo = []
        acyclic = True
        # initialize all nodes as white
        color = {k: Solution.white for k in range(numCourses)}
        
        def dfs(node):
            nonlocal acyclic
            # if there is a cycle, then not possible
            if not acyclic:
                return 
            color[node] = Solution.gray
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.white:
                        dfs(neighbor)
                    # an edge to gray node represents a cycle
                    elif color[neighbor] == Solution.gray:
                        acyclic = False
            color[node] = Solution.black
            topo.append(node)
        
        for vertex in range(numCourses):
            if color[vertex] == Solution.white:
                dfs(vertex)
                
        return topo[::-1] if acyclic else []

# solution 2: node indegree, add all nodes with 0-indegree to deque
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        
        topo = []
        zero_indegree_deque = deque([k for k in range(numCourses) if k not in indegree])
        # reduce the indegree of neighbor
        while zero_indegree_deque:
            vertex = zero_indegree_deque.popleft()
            topo.append(vertex)
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree_deque.append(neighbor)
                
        return topo if len(topo) == numCourses else []

if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [0,1]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,2,1,3]

        
            