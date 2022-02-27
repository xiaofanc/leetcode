"""
Count the number of servers in each row to X
Count the number of servers in each col to Y
If X[i] + Y[j] > 2, the server at A[i][j] (if exists) communicate.
"""
class Solution:
    # Time: O(m*n), space: O(m+n)
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = [0]*m, [0]*n
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row[i] + col[j] > 2:
                    count += 1
        return count
        
    def countServers(self, A):
        X, Y = list(map(sum, A)), list(map(sum, zip(*A)))
        return sum(X[i] + Y[j] > 2 for i in range(len(A)) for j in range(len(A[0])) if A[i][j])

if __name__ == '__main__':
    s = Solution()
    print(s.countServers([[1,0],[1,1]]))  # 3