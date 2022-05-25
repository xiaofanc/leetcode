"""
We get the mimimum prices at each point, and calculate the max profit

       [7, 1, 5, 3, 6, 4]
min  = [7, 1, 1, 1, 1, 1]
maxp = [0, 0, 4, 2, 5, 5]

"""

class Solution:
    """ 
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                profit = prices[j] - prices[i]
                max_ = max(profit, max_)
        return max_
    """ 
    def maxProfit(self, prices):
        min_ = float('inf')
        max_ = 0
        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            max_ = max(max_, (prices[i] - min_))
        return max_
    
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        minprice, maxprofit = prices[0], 0
        for price in prices[1:]:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
            
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
