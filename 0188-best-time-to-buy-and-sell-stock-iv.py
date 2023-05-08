"""
最多进行k次交易时的最大收益。one stock each time。
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0 or k == 0:
            return 0

        def maxProfit_k_inf(prices):
            # 122. 不限交易次数, one stock each time
            # return sum((a-b) for a, b in zip(prices[1:], prices) if a-b>0)
            n = len(prices)
            dp = [[0 for j in range(2)] for i in range(n)]
            for i in range(n):
                # base case
                if i == 0:
                    # 第一天没有股票时的最大收益
                    dp[i][0] = 0
                    # 第一天有股票时的最大收益
                    dp[i][1] = -prices[i]
                    continue
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            return dp[n-1][0]
        
        if k > n/2:
            # 相当于不限交易次数
            return maxProfit_k_inf(prices)
        
        # dp[i][j][0]: 在第i天共交易j次之后没有股票时的最大收益
        # dp[i][j][1]: 在第i天共交易j次之后有股票时的最大收益
        # why float('-inf') ? to mark impossible cases like dp[0][0][1]
        dp = [[[float('-inf') for i in range(2)] for j in range(k+1)] for i in range(n)]
        # base case
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1, n):
            for j in range(k+1):
                # 卖股票是j次交易的一部分，所以是dp[i-1][j][1] rather than dp[i-1][j-1][1]
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])     
                # 如果有股票，可能是前一天买的
                # # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        
        # 最多进行k次交易的最大profit
        res = max(dp[n-1][j][0] for j in range(k+1))
        return res
        
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k,0,-1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[n-1][k][0]


                    