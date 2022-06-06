"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

valid tree: all nodes are connected & no cycle

"""

class Solution:
	# not pass
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        # if there is a node not connected
        # 4, [[0,1],[2,3]] - not pass
        if len(adj_list) < n:
            return False
        # check cycle
        # comb是局部变量，不能track nodes are all connected
        def dfs(n, comb):
            if len(comb) >= 2 and n == comb[-2]:
                return
            elif n in set(comb):
                return True
            
            comb.append(n)
            for nei in adj_list[n]:
                if dfs(nei, comb):
                    return True
            comb.pop()
        for i in range(n):  # wrong，只能查cycle
            if dfs(i, []):
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        # print("adj_list", adj_list)
        # check cycle
        visited = set()
        def dfs(n, prev):
            if n in visited:
                return False # cycle
            
            visited.add(n)
            for nei in adj_list[n]:
                if nei == prev:  # [0,1,0] - avoid visit previous node
                    continue
                if not dfs(nei, n):
                    return False
            return True
            
        return dfs(0, -1) and n == len(visited)  # check all nodes are connected          

if __name__ == '__main__':
 	s = Solution()
 	print(s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) 
 	print(s.validTree(4, [[0,1],[2,3]])) 



 	
