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

if __name__ == '__main__':
	s = Solution()
	print(s.maxA(7))  # 9