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
            buy [i] = max(rest[i-1]-prices[i], buy[i-1])
            sell[i] = max( buy[i-1]+prices[i], sell[i-1])
            rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
        return sell[-1]
        
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]) == 3)