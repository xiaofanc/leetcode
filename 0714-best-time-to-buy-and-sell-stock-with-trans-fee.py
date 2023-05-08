
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0]到当前i天为止手中无股票最大的profit
        # dp[i][1]到当前i天为止手中有股票最大的profit
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee) # selling a stock needs transaction fee
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[n-1][0]


