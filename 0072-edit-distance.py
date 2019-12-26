class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1)+1, len(word2)+1
        dp = [[0]*L2 for _ in range(L1)]
        for i in range(L1): dp[i][0] = i
        for j in range(L2): dp[0][j] = j
        for i in range(1, L1):
            for j in range(1, L2):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        return dp[-1][-1]

        
if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse","ros") == 3)