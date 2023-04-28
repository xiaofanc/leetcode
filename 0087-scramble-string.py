# For each given dp state, we need 3 variables: length, i, and j.
# Each state will focus on two substrings. The first one will be a substring of s1, starting at index i with length equal to length - let's call this substring s. The second one will be a substring of s2, starting at index j with length - let's call this substring t.
# base case: dp[1][i][j] = (s1[i] == s2[j])
# if not swap, in order to make dp[length][i][j] return True, we need: dp[newLength][i][j] = True & dp[length - newLength][i + newLength][j + newLength] = True
# if swap, we need: dp[newLength][i][j+length-newLength] = True & dp[length-newLength][i+newLength][j] = True
# The answer to the problem is dp[n][0][0], as starting at index 0 with length n is considering the entire input string.

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)] for l in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = (s1[i] == s2[j])
        
        for length in range(2, n+1):
            for i in range(n+1-length):
                for j in range(n+1-length):
                    for newl in range(1, length):
                        dp1 = dp[newl][i]
                        dp2 = dp[length-newl][i+newl]
                        dp[length][i][j] |= dp1[j] and dp2[j+newl]
                        dp[length][i][j] |= dp1[j+length-newl] and dp2[j]
        return dp[n][0][0]
