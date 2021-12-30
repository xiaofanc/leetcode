"""
fibonacci number:
f(n) = f(n-1) + f(n-2)

"""
class Solution:
    # Space: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev, curr = 1, 2
        for i in range(n-2):
            prev, curr = curr, prev + curr
        return curr

    # Space: O(n)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n          
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3) == 3)