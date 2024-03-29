"""
fibonacci number:
f(n) = f(n-1) + f(n-2)

stair 1: 1 -> prev
stair 2: 2 -> cur
stair 3: 1+2 = 3
stair 4: 2+3 = 5
stair 5: 3+5 = 8

update cur n-2 times.. return cur

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

    def climbStairs(self, n: int) -> int:  # same as fibo
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

    