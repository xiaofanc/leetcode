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
        # (i,total) -> # of ways
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
        
if __name__ == '__main__':
	s = Solution()
	print(s.findTargetSumWays([1,1,1,1,1])) # 3
    
                     