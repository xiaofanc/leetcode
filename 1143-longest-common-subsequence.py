"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

"""
def memo(f):
    m = {}
    def wrapper(*args):
        if args not in m:
            m[args] = f(*args)
        return m[args]
    return wrapper

class Solution:
    # top down DP
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time: O(m*n)
        @memo
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1+1, p2+1)
            else:
                return max(memo_solve(p1+1, p2), memo_solve(p1, p2+1))
        
        return memo_solve(0, 0)

    # dp[i][j] = LCS for text1[:i] and text2[:j]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # print(i,j)
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # print(dp)
        return dp[m][n]

    # bottom up DP
    # dp[i][j] = LCS for text1[i:] and text2[j:]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)] # LCS(“abcde”, “”)
        # print("dp->", dp)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # LCS(“abcde”, “ace”) = 1 + LCS(“bcde”, “ce”)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # LCS(“abcde”, “dce”) = max(LCS(“abcde”, “ce”), LCS(“bcde”, “dce”))
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace")) # 3


