from collections import defaultdict, deque
class Solution:
    # Time = Space = O(E+V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        
        topo = []
        zero_indegree_deque = deque(k for k in range(numCourses) if k not in indegree)
        while zero_indegree_deque:
            node = zero_indegree_deque.popleft()
            topo.append(node)
            neighbors = adj_list[node]
            for n in neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    del indegree[n]
                    zero_indegree_deque.append(n)
        return True if len(topo) == numCourses else False
    
    # Time = Space = O(E+V)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
            
        path = [False] * numCourses
        checked = [False] * numCourses
        for cur in range(numCourses):
            if self.isCycle(cur, adj_list, path, checked):
                return False
        return True
    
    def isCycle(self, cur, adj_list, path, checked):
        # bottom cases
        if checked[cur]:
            return False
        if path[cur]:
            return True
        
        path[cur] = True
        ret = False
        for neighbor in adj_list[cur]:
            ret = self.isCycle(neighbor, adj_list, path, checked)
            if ret: break
        # remove node from path
        path[cur] = False
        
        # node is checked
        checked[cur] = True
        return ret

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq map
        premap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visitedSet = set()
        # check each course
        def dfs(crs):
            # if cycle is detected
            if crs in visitedSet:
                return False
            # if no prereq or can be taken
            if crs == []: 
                return True
            # else
            visitedSet.add(crs)
            for nei in premap[crs]:
                if not dfs(nei): return False
            # 3->[4,5], 6->[3]
            visitedSet.remove(crs)
            premap[crs] = [] # course can be taken
            return True

        # 1->2, 3->4, therfore we have to check every course
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1,0]])) # True
    print(s.canFinish(2, [[1,0],[0,1]])) # False