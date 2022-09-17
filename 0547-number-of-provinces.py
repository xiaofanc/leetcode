"""
 [1 0 0 1]
 [0 1 1 0]
 [0 1 1 1]
 [1 0 1 1]

A -> D -> C -> B
Each row is a node and each column means whether the node has next

"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [] # row visited
        count = 0
        # dfs starts from every new node
        for row in range(len(isConnected)):
            if row not in visited:
                count += 1
                self.dfs(row, isConnected, visited)
        return count
    
    def dfs(self, r, grid, visited):
        # dfs searches next connected node
        visited.append(r)
        for c in range(len(grid)):
            if grid[r][c] == 1 and c not in visited:
                # then visit that c row
                self.dfs(c, grid, visited)

if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))  # 1





