"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

1 0  1 0 0
1 0 |1 1| 1
1 1 |1 1| 1
1 0  0 1 0

output: 4

We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.

dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as

dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.

dp:
1 0 1 0 0
1 0 1 1 1
1 1 1 2 2 
1 0 0 1 0

"""

class Solution:  # time: O(mn)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        height, width = len(matrix), len(matrix[0])
        dp = [[0]*width for i in range(height)]
        maxlen = 0
        for i in range(height):
            if matrix[i][0] == '1': 
                dp[i][0] = 1
                maxlen = 1
        for j in range(width):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                maxlen = 1
        #print(dp)
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
                    maxlen = max(dp[i][j], maxlen)
        #print(dp)
        return maxlen*maxlen

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = int(matrix[i][j])
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len
        
if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 4
