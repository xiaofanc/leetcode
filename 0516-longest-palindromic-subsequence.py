# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""
Let dp(l, r) denote the length of the longest palindromic subsequence of s[l..r].
There are 2 options:
If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
Then dp(0, n-1) is our result.
"""

class Solution:

	# Time: O(N^2), Space: O(N^2)
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @lru_cache(None)
        # dp(l, r): the length of the longest palindromic subsequence of s[l..r].
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dp(i+1, j-1) + 2
            return max(dp(i+1, j), dp(i, j-1))
        
        return dp(0, len(s)-1)


    def longestPalindromeSubseq(self, s: str) -> int:
            n = len(s)
            
            cache = {}
            def helper(l, r):
                if (l,r) in cache: return cache[(l,r)]
                if l > r: return 0
                if l == r: return 1
                if s[l] == s[r]:
                    cache[(l,r)] = helper(l + 1, r - 1) + 2
                    return cache[(l, r)]
                cache[(l,r)] = max(helper(l, r - 1), helper(l + 1, r))
                return cache[(l, r)]

            return helper(0, n - 1) 

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[1]*len(s) for _ in range(len(s))]
        res = 1
        for j in range(len(s)):
            for i in range(j-1,-1,-1):
                if i == j-1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1] , dp[i+1][j])
                
                res = max(res, dp[i][j])
        return res
                
if __name__ == '__main__':
	s = Solution()
	print(s.longestPalindromeSubseq("bbbab"))  #4



