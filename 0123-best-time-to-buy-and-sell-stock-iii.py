"""
交易两次最大profit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, buy, act):
            # max profit starts from prices[i] with number of sell/buy = act, next action = buy
            if (i, buy, act) in memo:
                return memo[(i, buy, act)]
            if i == len(prices) or act > 4:
                return 0
            profit = 0
            if buy:
                profit = max(-prices[i] + helper(i+1, False, act+1), helper(i+1, True, act))
            else:
                # sell
                profit = max(prices[i] + helper(i+1, True, act+2), helper(i+1, False, act))
            memo[(i, buy, act)] = profit
            return profit
        return helper(0, True, 0)

"""
dp[i][k][0 or 1]
0 <= i <= n - 1, 1 <= k <= K
n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票。

状态转移方程：
到当前i天为止进行k次交易后手中无股票的最大profit:
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
到当前i天为止进行k次交易后手中有股票的最大profit:
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

base case：
dp[-1][...][0] = dp[...][0][0] = 0
dp[-1][...][1] = dp[...][0][1] = -infinity
"""

    def maxProfit(self, prices: List[int]) -> int:
        K = 2
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(n)]
        for i in range(n):
            for k in range(K, 0, -1):
                if i == 0:
                    # base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][K][0]


