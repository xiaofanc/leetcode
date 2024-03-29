"""
sol1: DFS/backtracking: TLE

sol2: top down dynamic programming 
coins: [1,2,5]
what is the minimum number of coins to sum up to 0?
dp(0) = 0
dp(1) = 1
dp(2) = 1+dp(1)
dp(3) = min(1+dp(3-1), 1+dp(3-2))
dp(4) = min(1+dp(4-1), 1+dp(4-2))
...
dp(7) = min(1+dp(7-1), 1+dp(7-2), 1+dp(7-5))

dp(i)可以无解

"""

class Solution:  # time O(n*k) k=# of coins  n=0-amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # dp[i] = amount+1 不可能取到
        dp[0] = 0 # in order to make the math work
        
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], 1+dp[i-c])
        return dp[amount] if dp[amount] != amount+1 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for amt in range(coin, amount+1):
                dp[amt] = min(dp[amt], 1+dp[amt-coin])
        return dp[amount] if dp[amount] != amount+1 else -1
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        #dp[i] is the min combination sums up to amount i
        for amt in range(1, amount+1):
            minc = float('inf')
            for c in coins:
                #print('amt: ', amt, 'c: ', c, 'dp[amt-c]: ', dp[amt-c])
                if amt-c >= 0 and dp[amt-c] != -1: # dp[amt-c] has solution
                    opt = dp[amt-c] + 1            # 1 option => 1, 2, 5
                    minc = min(opt, minc)          # find the min among solutions
                    #print('opt:%d , minc: %d' % (opt, minc))
                if minc != float('inf'): 
                    dp[amt] = minc
            #print('dp[amt]: ', dp[amt])
        return dp[-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        #dp[i] is the min combination sums up to amount i
        for amt in range(1, amount+1):
            options = [dp[amt-c] for c in coins if amt-c >= 0 and dp[amt-c] != -1]
            if options != []:
                dp[amt] = min(options) + 1
        return dp[-1]
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1

    # no cache: O(kxn^k), cache: O(nxk)
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1:
                    continue
                res = min(res, 1+subproblem)
            return res if res != float('inf') else -1
        
        return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[amount+1 for j in range(amount+1)] for i in range(n+1)]

        # dp[i][j] => 从前i个数之中取数取得sum=j的最少硬币数
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    # min(用前i-1个数构成j， 用前i个数构成j)
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
        return dp[n][amount] if dp[n][amount] != amount+1 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount+1 for i in range(amount+1)]

        # base case: sum = 0
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], 1+dp[j-coins[i]])
                    
        return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5]), 11)  #3
    print(s.coinChange([2]), 3)  # -1
    # dp [0, 4, 4, 4]
    # dp [0, 4, 1, 4]
    # dp [0, 4, 1, 4]




