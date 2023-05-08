"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to target.

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""
class Solution:
	# recursion with caching
	# Time = space = O(n x t), t = sum(nums), possible sum is [-sum(nums), sum(nums)]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # (i,total) -> # of ways to reach target since i and total
        # start from i and total value, how many ways we can get to the target 
        dp = {}
        def backtracking(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = backtracking(i+1, total+nums[i]) + backtracking(i+1, total-nums[i])
            return dp[(i, total)]
        return backtracking(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, curSum):
            if i == len(nums) and curSum == target:
                return 1
            # if curSum > target:  # can -1 afterwards
                # return 0
            if i == len(nums):
                return 0
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            memo[(i, curSum)] = dfs(i+1, curSum+nums[i]) + dfs(i+1, curSum-nums[i])
            return memo[(i, curSum)]
        return dfs(0, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # [100], -200
        if sum(nums) < target or (sum(nums) + target) % 2 or -sum(nums) > target:
            return 0

        def subsetsum(s):
            dp = [[0 for j in range(s+1)] for i in range(n+1)]

            for i in range(n+1):
                dp[i][0] = 1
            
            for i in range(1, n+1):
                for j in range(s+1):
                    # print("j->", i, j)
                    if j < nums[i-1]:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
            return dp[n][s]
        
        s = (sum(nums)+target)//2 # s >= 0
        return subsetsum(s)        

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # [100], -200
        if sum(nums) < target or (sum(nums) + target) % 2 or -sum(nums) > target:
            return 0

        def subsetsum(s):
            dp = [0 for j in range(s+1)]

            dp[0] = 1
            
            for i in range(1, n+1):
                # start from backwards
                for j in range(s,-1,-1):
                    if j < nums[i-1]:
                        dp[j] = dp[j]
                    else:
                        dp[j] = dp[j] + dp[j-nums[i-1]]
            return dp[s]
        
        s = (sum(nums)+target)//2 # s >= 0
        return subsetsum(s)

if __name__ == '__main__':
	s = Solution()
	print(s.findTargetSumWays([1,1,1,1,1])) # 3
    
                     