class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        dp = [[float("inf")] * len(mat[0]) for i in range(len(mat))]
        # first pass: check for top and left
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        
        # second pass: check for bottom and right
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] != 0:
                    if i < len(mat)-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                    if j < len(mat[0])-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        return dp

# inplace
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        # first pass: check for top and left
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    mat[i][j] = float("inf")
                    if i > 0:
                        mat[i][j] = min(mat[i][j], mat[i-1][j]+1)
                    if j > 0:
                        mat[i][j] = min(mat[i][j], mat[i][j-1]+1)
        
        # second pass: check for bottom and right
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] != 0:
                    if i < len(mat)-1:
                        mat[i][j] = min(mat[i][j], mat[i+1][j]+1)
                    if j < len(mat[0])-1:
                        mat[i][j] = min(mat[i][j], mat[i][j+1]+1)
        return mat

if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
    print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]


