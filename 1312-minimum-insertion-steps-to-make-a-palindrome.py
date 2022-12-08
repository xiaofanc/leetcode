class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            # min insertion for s[i:j]
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= j:
                return 0
            if s[i] == s[j]:
                memo[(i, j)] = dp(i+1, j-1)
            else:  # "xaaaa"
                memo[(i, j)] = min(dp(i+1, j), dp(i, j-1)) + 1
            return memo[(i, j)]
        return dp(0, len(s)-1)
