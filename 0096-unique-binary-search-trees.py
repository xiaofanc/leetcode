"""
dp[i] = dp[j] * dp[i-j-1]
dp[0] = 1
dp[1] = dp[0] * dp[0]
dp[2] = dp[0] * dp[1] + 
        dp[1] * dp[0]
dp[3] = dp[0] * dp[2] + 
        dp[1] * dp[1] + 
        dp[2] * dp[0]
....

"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        # base case: 
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[-1]

    def numTrees(self, n: int) -> int:
        dp = [1]
        for i in range(1, n+1):
            dp.append(sum(dp[j]*dp[i-j-1] for j in range(i)))
        return dp[-1]


                
                
if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3) == 5)