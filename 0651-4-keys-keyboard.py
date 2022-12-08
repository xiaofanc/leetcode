"""
dp[i] is the maximum 'A' after i moves
dp[i] = max(dp[i-1]+1, dp[i-2]*1, dp[i-3]*2, dp[i-4]*3....)
"""

class Solution:
    def maxA(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n+1):
            cur = dp[i-1] + 1
            for y in range(i-1):
                # print("y->", y)
                cur = max(cur, dp[y]*(i-y-1))
            dp.append(cur)
        return dp[-1]

    # sol-1: TLE -> C-A + C-C, C-A + C-C, C-A + C-C... - no need to consider
    def maxA(self, n: int) -> int:
    memo = {}
    # n - operations left, A_num - number of A on the screen, copy - number of A in the clip board
    def dp(n, A_num, copy):
        if n <= 0:
            return A_num
        memo[(n, A_num, copy)] = max(
            dp(n-1, A_num+1, copy), # A
            dp(n-1, A_num+copy, copy), # C-V
            dp(n-2, A_num, A_num)  # C-A + C-C
            )
        return memo[(n, A_num, copy)]
    return dp(n, 0, 0)

    # sol-2: best sceneria -> A,A,....C-A, C-C, C-V, C-V, ....C-A, C-C, C-V, C-V...
    def maxA(self, n: int) -> int:
        memo = {}
        def dp(i): # number of operrations left
            if i <= 0:
                return 0
            if i in memo:
                return memo[i]
            # press A in i
            res = dp(i-1)+1
            # press C-V in i
            for j in range(2, i): # when is C-A, C-C
                # get the copy for C-A, C-C, number of A = dp[j-2]
                res = max(res, dp(j-2)*(i-j+1))
            memo[i] = res
            return res
        
        return dp(n)

if __name__ == '__main__':
	s = Solution()
	print(s.maxA(7))  # 9