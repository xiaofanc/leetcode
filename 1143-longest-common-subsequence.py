def memo(f):
    m = {}
    def wrapper(*args):
        if args not in m:
            m[args] = f(*args)
        return m[args]
    return wrapper

class Solution:
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

    # dp[i][j] represents 到第一个字符串位置 i 为止、到 第二个字符串位置 j 为止、最长的公共子序列长度
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

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace")) # 3


