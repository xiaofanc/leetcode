"""
count groups for matrix M
M[i][j] = "1" means i and j is in a group
M = 
110
110
001

There are 2 groups ([0,1], [2]) in M
"""
class Solution:
    def countGroups(related):
        # Write your code here
        rows, cols = len(related), len(related[0])
        adj = {i:set() for i in range(rows)}
        for i in range(rows):
            for j in range(cols):
                if i != j and related[i][j] == "1":
                    adj[i].add(j)
                    adj[j].add(i)
        visited = set()    
        def dfs(n, prev):
            if n in visited:
                return
            visited.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue
                dfs(nei, n)
            return
        
        count = 0
        for i in range(rows):
            if i in visited:
                continue
            else:
                count += 1
                dfs(i,-1)
        return count
        
                
if __name__ == '__main__':
    arr = ["1100", "1110", "0110", "0001"]
    s = Solution()
    print(s.countGroups(arr))  # 2 -> [[0,1,2],[3]]
