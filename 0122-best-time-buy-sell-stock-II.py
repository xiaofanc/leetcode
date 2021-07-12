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

s=Solution()
print(s.maxProfit0([7,1,5,6,4,7,4,9,1]))
print(s.maxProfit1([7,1,5,6,4,7,4,9,1]))
print(s.maxProfit2([7,1,5,6,4,7,4,9,1]))







