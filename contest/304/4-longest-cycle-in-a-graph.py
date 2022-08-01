
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def dfs(node, path, l):
            nonlocal maxl
            # print("path", node, path, l)
            if node == -1:
                return
            if node in visited:
                # check if node in the path
                idx = -1
                for i, n in enumerate(path):
                    if n == node:
                        idx = i
                if idx == -1:
                    return
                else:
                    maxl = max(maxl, l-idx)
                    # print("l, idx, maxl", l, idx, maxl)
                    return
            visited.add(node)
            path.append(node)
            dfs(edges[node], path, l+1)
                
        maxl = -1
        visited = set()
        for node in range(len(edges)):
            dfs(node, [], 0)
        return maxl
            

    def longestCycle(self, edges: List[int]) -> int:
        # Time: O(N)
        # cycle will be visited once
        # each node will be visited once
        def dfs(node, idx, path, l):
            nonlocal maxl
            if node == -1: # no cycle
                return
            if node in visited:
                # get the index of node if it is in the path
                i = idx.get(node, -1)
                # node is not in the path, but visited in previous path
                # no need to continue
                if i == -1:
                    return
                else:
                    maxl = max(maxl, l-i)
                    return
            idx[node] = l
            visited.add(node)
            path.append(node)
            dfs(edges[node], idx, path, l+1)
                
        maxl = -1
        visited = set()           # global
        for node in range(len(edges)):
            idx = defaultdict()   # local
            dfs(node, idx, [], 0)
        return maxl

    def longestCycle(self, edges: List[int]) -> int:
        # Time: O(N)
        # cycle will be visited once
        # each node will be visited once
        def dfs(node, idx, l):
            nonlocal maxl
            # if no cycle or node is visited in the previous path
            # [2,3,4] will return
            if node == -1 or node in visited:
                return
            idx[node] = l
            visited.add(node)
            node = edges[node]
            l += 1
            # get the index of node if it is in the path
            i = idx.get(node, -1)
            if i != -1:
                maxl = max(maxl, l-i)
                return
            dfs(node, idx, l)
            
        maxl = -1
        visited = set()           # global
        for node in range(len(edges)):
            idx = defaultdict()   # local
            dfs(node, idx, 0)
        return maxl

    # Time: O(n)
    def longestCycle(self, edges: List[int]) -> int:
        # since each node has only one edge, it can only exist in one cycle
        # if input is [3,3,4,2,3]
        trav = [False]*len(edges)
        ans = -1
        for i in range(len(edges)):
            # if node is not visited
            # will only visit 0, 1 since 2,3,4 was visited when start from 0
            if not trav[i]:
                curr, dis, disMap = i, 0, {}
                while curr != -1 and not trav[curr]: # when visiting from 1, 2 was visited so it will not continue
                    trav[curr] = True
                    disMap[curr] = dis  # save the index for cur node in the path
                    curr = edges[curr]  # move to the next node
                    dis += 1
                    
                    if curr in disMap:  # [0,3,2,4,3]
                        ans = max(ans, dis - disMap[curr]) # 4-1=3
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.longestCycle([2,-1,3,1])) # -1    
    # only [0,3,7] will be checked, other node will directly return since they were visited in the previous path
    print(s.longestCycle([1,2,0,4,5,6,3,8,9,7])) # 4 [0,1,2,0], [3,4,5,6,3], [7,8,9,7]



