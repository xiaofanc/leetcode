"""
交易无限次最大profit
peak-valley approach:
The key point is we need to consider every peak immediately following a valley to maximize the profit. In case we skip one of the peaks (trying to obtain more profit), we will end up losing the profit over one of the transactions leading to an overall lesser profit.
"""

from typing import List
class Solution:
    def maxProfit0(self, prices: List[int]) -> int:
        return sum(max([prices[i+1]-prices[i],0]) for i in range(len(prices)-1))

    def maxProfit1(self, prices: List[int]) -> int:
        return sum([b-a for a,b in zip(prices,prices[1:]) if b-a > 0])

    def maxProfit2(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        max_profit, buy, sell = 0, -1, -1
        for i in range(0, length):
            if i + 1 == length:
                max_profit += sell - buy
                continue
            if prices[i+1] > prices[i]:
                sell = prices[i+1]
                if buy == -1:
                    buy = prices[i]
            else:
                max_profit += sell - buy
                sell = -1
                buy = -1
        return max_profit

    def maxProfit3(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i]-prices[i-1]
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        # peak valley approach
        valley, peak = prices[0], prices[0]
        i, maxProfit = 0, 0
        while i < len(prices)-1:
            # find the valley first
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # then find the peak
            #print(i)
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            #print(valley, peak)
            maxProfit += peak - valley
               
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0]到当前i天为止手中无股票最大的profit
        # dp[i][1]到当前i天为止手中有股票最大的profit
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

s=Solution()
print(s.maxProfit0([7,1,5,6,4,7,4,9,1]))
print(s.maxProfit1([7,1,5,6,4,7,4,9,1]))
print(s.maxProfit2([7,1,5,6,4,7,4,9,1]))







