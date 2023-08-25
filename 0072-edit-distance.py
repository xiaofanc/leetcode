"""
solution 2: bottom up DP
base cases: 
1. word1 = "", word2 = "abc", res = len(word2)
2. word1 = "abc", word2 = "", res = len(word1)
3. word1 = "", word2 = "", res = 0
        i
word1: "abc"
word2: "adc"
        j
if word1[i] == word2[j]:
    (i+1, j+1)
else: 1 + min(...)
insert: (i, j+1)
delete: (i+1, j)
replace: (i+1, j+1)

dp[i][j]: min number of operations that convert word1[i:] to word2[j:]

example:
    word1 = "horse", word2 = "ros"
       h  o  r  s  e 
r    [[3, 3, 2, 3, 3, 3],  # dp[0][5] = convert "" to "ros" = 3
o     [3, 2, 2, 2, 2, 2],  # dp[0][4] = convert "" to "os" = 2
s     [4, 3, 2, 1, 1, 1], 
      [5, 4, 3, 2, 1, 0]]
          # dp[3][1] = convert "orse" to "" = 4

"""
class Solution:
    # dp[i][j]: min number of operations that convert word1[:i] to word2[:j]
    def minDistance(self, word1: str, word2: str) -> int:
        L1, L2 = len(word1)+1, len(word2)+1
        dp = [[0]*L2 for _ in range(L1)]
        for i in range(L1): dp[i][0] = i
        for j in range(L2): dp[0][j] = j
        for i in range(1, L1):
            for j in range(1, L2):
                # dp[1][1] = # convert word1[0] to word2[0]
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        return dp[-1][-1]

    # dp[i][j]: min number of operations that convert word1[i:] to word2[j:]
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][n] = len(word1[i:]) # word2 = ""
        for j in range(n):
            dp[m][j] = len(word2[j:]) # word1 = ""
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) + 1
        return dp[0][0]

    # top down DP
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j == len(word2):
                return len(word1[i:])
            if i == len(word1):
                return len(word2[j:])
            if word1[i] == word2[j]:
                res = dfs(i+1, j+1)
            else:
                res = min(dfs(i,j+1), dfs(i+1,j), dfs(i+1, j+1)) + 1
            cache[(i,j)] = res
            return res
        return dfs(0,0)

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("horse","ros") == 3)


