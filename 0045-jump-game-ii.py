"""
Return the minimum number of jumps to reach nums[n - 1]
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        def backtrack(i):
            if i >= len(nums)-1:
                return 0
            if dp[i] != float('inf'):
                return dp[i]
            for j in range(1, nums[i]+1):
                dp[i] = min(dp[i], 1+backtrack(i+j))
            return dp[i]
        
        return backtrack(0)

    # dp[i] denotes minimum jumps required from current index to reach till the end
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0 # no more step is needed
        n = len(nums)
        for i in range(n-2,-1,-1):
            for j in range(i+1, min(i+nums[i]+1, n)):
                dp[i] = min(dp[i], 1+dp[j])
        return dp[0]

