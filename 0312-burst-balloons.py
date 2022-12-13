"""
same as matix multiplication： Divide and Conquer, and Thinking Backwards.

1. Add one balloon at the start of nums and one at the end to handle edge cases.

2. Define a function dp to return the maximum coins obtainable, if we burst all balloons on the interval [left, right], inclusively.

3. The base case is that the interval is empty, which yields 0 coin.

For general cases, we iterate over every index i in [left, right], and mark the balloon at that index as the last one burst in order to make subproblem independent.

First, We burst all balloons except the ith one. What we gain is:
dp(left, i - 1) + dp(i + 1, right)

Then, we burst the ith one:
nums[left - 1] * nums[i] * nums[right + 1]

Just return the maximum sum of those two among all possible is.

4. Finally, return dp(1, len(dp) - 2).

Do not return dp(0, len(dp) - 1) since the first and the last balloons were added by us and we cannot burst them.

Time: O(N^3), Space: O(N^2)
"""
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
    memo = {}
    nums = [1] + nums + [1]

    def dp(i, j): # maxCoins to burn balloons in [i, j] inclusive
        if i > j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        res = 0
        for k in range(i, j+1):
            gain = nums[k]*nums[i-1]*nums[j+1] # last balloon
            left = dp(i, k-1) + dp(k+1, j) # subp is independent since right of k-1 is k
            res = max(res, gain+left)
        memo[(i, j)] = res
        return memo[(i, j)]
    
    return dp(1, len(nums)-2)

    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        # maxCoins to burn balloons in [i, j] inclusive
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1]+dp[k+1][j]+nums[k]*nums[i-1]*nums[j+1])
        return dp[1][n] 

    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]

        def dp(i, j): # maxCoins to burn ballons in (i, j) exclusive
            if i >= j-1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = 0
            for k in range(i+1, j):
                gain = nums[k]*nums[i]*nums[j] # last balloon
                left = dp(i, k) + dp(k, j) # subproblem is independent
                res = max(res, gain+left)
            memo[(i, j)] = res
            return memo[(i, j)]
        
        return dp(0, len(nums)-1)

    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        nums = [1] + nums + [1]

        # maxCoins to burn balloons in (i, j) exclusive
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j): # k = i+1 -> j-1
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[k]*nums[i]*nums[j])
        return dp[0][n+1]

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)-1
        dp = [[0]*n for _ in range(n)]
        for w in range(1, n):
            for i in range(n-w):
                j = i + w
                maxcost = max(dp[i][l]+dp[l+1][j]+nums[i]*nums[l+1]*nums[j+1] for l in range(i, j))
                dp[i][j] = maxcost
        return dp[0][-1]
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,1,5,8]) == 167)