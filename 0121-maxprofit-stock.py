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
    
    
    
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
