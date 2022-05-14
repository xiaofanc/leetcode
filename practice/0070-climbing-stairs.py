"""
dp[i] = dp[i-2] + dp[i-1]

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, cur = 1, 1
        for i in range(2, n+1):
            # dp[i] = dp[i-1] + dp[i-2]
            prev, cur = cur, prev+cur
        return cur

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3) == 3)
    
	