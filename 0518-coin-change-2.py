"""
To understand how the coin loop being outside resolves the double counting, you should pay attention to the fact that when the coin loop is outside, we will count how many combinations are possible with say 2c coin and then add that number to the ways in which the same amount can be created using 3c coin. This imposition of order removes the double counting

Compare that with the situation where the coins are in the inner loop. Here we would calculate how many ways we can create an amount using all coins (i.e. 1 and 2 both) and then for the next amount of interest, we will count using all coins (i.e. 1 and 2 both). As you see, we are counting both 1c after 2c and 2c after 1c scenarios, causing the double counting.
"""
``
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            # how many ways to create x using coin
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]
                # print("dp", coin, dp)                
        return dp[amount]

if __name__ == '__main__':
	s = Solution()
	print(s.change(5, [1,2,5])) # 4: [5,0],[2,2,1],[2,1,1,1],[1,1,1,1,1]