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

    # greedy
    # [3, 1, 4, 2, ....]; 为了得到最少step，肯定选择[1, 4, 2]中能够到达的最远距离
    def jump(self, nums: List[int]) -> int:
        # 记录i...end能够跳到的最远的地方
        end = farthest = 0
        jumps = 0
        for i in range(len(nums)-1):
            farthest = max(i+nums[i], farthest)
            # checked all possible spots
            if i == end:
                jumps += 1
                end = farthest # check next interval
        return jumps

