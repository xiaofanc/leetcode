"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
|rabb|b|it|
|rab|b|bit|
|ra|b|bbit|

if s[i] == t[j]: check (i+1, j+1) -> does not mean next (i+1) could not match
Therefore, check (i+1, j) as well
else: check (i+1, j) why? we need to match t

base case: s = "", t = "" => return 1
		   s = "abv", t = "" => return 1
		   s = "", t = "abd" => return 0
"""

class Solution:
	# Time = space = O(MxN)
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i,j):
            # number of ways to generate t[j:] from s[i:]
            if (i,j) in cache:
                return cache[(i,j)]
            # base cases:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1) + dfs(i+1, j)
            else:
                res += dfs(i+1, j)
            cache[(i,j)] = res
            return res
        return dfs(0,0)

    def numDistinct(self, s: str, t: str) -> int:
        # if s[i] == t[j], dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
        # else dp[i][j] = dp[i+1][j]
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n] = 1 # t = ""
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
        
class Solution:
    # 61 / 65 testcases passed
    # worst time: O(n^n)
    def numDistinct(self, s: str, t: str) -> int:
        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)
        cache = {}

        def dfs(i,j):
            # number of ways to generate t[j:] from s[i:]
            # print("i, j, ", i, j)
            if (i,j) in cache:
                return cache[(i,j)]
            # base cases:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            res = 0
            for nexti in indexes[t[j]]:
                # print("nexti, ", nexti)
                if nexti >= i:
                    res += dfs(nexti+1, j+1)
            cache[(i,j)] = res
            return res
        return dfs(0,0)

if __name__ == '__main__':
	s = Solution()
	print(s.numDistinct("rabbbit", "rabbit")) # 3





