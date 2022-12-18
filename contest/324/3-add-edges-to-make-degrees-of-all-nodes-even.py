"""
20
[[2,7],[6,20],[7,19],[12,13],[4,9],[11,20],[11,13],[3,6],[3,7],[3,4],[1,8],[18,4],[16,6],[6,11],[9,16],[15,4],[13,3],[14,3],[18,12],[8,14],[15,2],[7,15],[4,11],[13,20],[20,18],[20,10],[20,3],[15,3],[4,8],[10,1],[19,15]]

adj  8 {1, 4, 14}
adj  18 {20, 4, 12}
adj  3 {4, 6, 7, 13, 14, 15, 20}
adj  15 {2, 3, 4, 7, 19}

return False is wrong. 
因为8和18配对了，所以3和15只能和even配对。这样有3条edge。
正确的配对方式是8-3，18-15或8-15，18-3.
"""
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # odd connects first? then both odds connect to even?
        # 46/47 passed
        adj = defaultdict(set)
        for src, dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
            # adj[src] = adj.get(src, 0) + 1
            # adj[dst] = adj.get(dst, 0) + 1
        
        odd = set()
        even = set()
        for k, v in adj.items():                
            if len(v) % 2 == 1:
                if len(v) == n-1:
                    return False
                else:
                    odd.add(k)
            else:
                even.add(k)
        
        # print("odd, even", odd, even)
        cnt = 0
        visited = set()
        for i in odd:
            for j in odd:
                if i != j and j not in adj[i] and i not in visited and j not in visited:
                    cnt += 1
                    visited.add(i)
                    visited.add(j)
                    # print("i, j", i, j)
        
        # for i in odd:
            # print("adj ", i, adj[i])
        
        for i in visited:
            odd.remove(i)
            
        if len(odd) == 0:
            return cnt <= 2
        else:
            return len(odd) == 2 and cnt == 0 and len(even) >= 1
            

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        # odd connects first? then both odds connect to even?
        # 46/47 pass
        adj = defaultdict(set)
        for src, dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        
        odd = []
        even = []
        for k, v in adj.items():                
            if len(v) % 2 == 1:
                if len(v) == n-1:
                    return False
                else:
                    odd.append(k)
            else:
                even.append(k)
        
        if len(odd) == 0:
            return True
        
        if len(odd) == 2:
            # pair together
            if odd[1] not in adj[odd[0]] and odd[0] not in adj[odd[1]]:
                return True
            else: # connect with even
                for e in even:
                    if odd[0] not in adj[e] and odd[1] not in adj[e]:
                        return True
                return False
        
        def valid(i, j):
            if i not in adj[j] and j not in adj[i]:
                return True
            return False

        if len(odd) == 4: # 只能两两配对
            if (valid(odd[0], odd[1]) and valid(odd[2], odd[3])) or (valid(odd[0], odd[2]) and valid(odd[1], odd[3])) or (valid(odd[0], odd[3]) and valid(odd[2], odd[1])):
                return True
            else:
                return False

            
            
            
            
        