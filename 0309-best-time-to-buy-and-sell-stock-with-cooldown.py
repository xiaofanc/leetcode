class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            # action before buy: rest, sell
            buy = max(prev_sell-price, prev_buy)
            prev_sell = sell
            # action before sell: rest, buy
            sell = max(prev_buy+price, prev_sell)
        return sell

    def maxProfit(self, prices: List[int]) -> int:
        # buy[i]  = max(rest[i-1]-price, buy[i-1])
        # sell[i] = max(buy[i-1]+price, sell[i-1])
        # rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        if len(prices) < 2:
            return 0
        n = len(prices)
        sell, buy, rest = [0]*n, [0]*n, [0]*n
        buy[0] = -prices[0]
        for i in range(1, n):
            # max profit when buy price[i]
            buy [i] = max(rest[i-1]-prices[i], buy[i-1])
            # max profit when sell price[i]
            sell[i] = max( buy[i-1]+prices[i], sell[i-1])
            # max profit when colling down
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        return sell[-1]

    def maxProfit(self, nums: List[int]) -> int:
        # (i, buying) to store if buy/sell in ith day
        # if buy -> i+1
        # if sell -> i+2
        dp = {}
        def dfs(i, buying):
            if i >= len(nums):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                # if buy, the next day cannot buy
                buy = dfs(i+1, not buying) - nums[i] 
                # if cooldown, the second day can still buy
                cooldown = dfs(i+1, buying)  
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # if sell, we must skip next day
                sell = dfs(i+2, not buying) + nums[i] 
                # if cooldown, the next day can still sell
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)

    def maxProfit(self, prices: List[int]) -> int:
        # initial state is reset
        # selling stock first is impossible
        # state machine
        sold, held, reset = float('-inf'), float('-inf'), 0
        for price in prices:
            prev_sold = sold
            sold = held + price
            held = max(held, reset-price)
            reset = max(reset, prev_sold)
        return max(sold, reset) # final state must be sold or reset

    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] = 到当前i天为止手中无股票的最大profit
        # dp[i][1] = 到当前i天为止手中有股票的最大profit
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            elif i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
                # 第i天手中有股票的max profit = Max(第i-1天手中有股票的max profit, 第i-2天手中没股票的max profit+买第i天的股票)
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[n-1][0]

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]) == 3)




    