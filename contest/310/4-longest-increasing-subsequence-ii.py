"""
2407.
"""

class Solution:
	# TLE: 71/86 passed
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        dp = [1]*(len(nums)+1)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j] and nums[j] - nums[i] <= k:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

	# TLE: 72/86 passed
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        dp = [0]*(100000+1)
        dp[nums[-1]] = 1
        for i in range(len(nums)-2,-1,-1):
            # print("num[i]", nums[i])
            dp[nums[i]] = 1
            for num in range(nums[i]+1, min(100001, nums[i]+k+1)):
                # print("num[j]->", num, dp[num])
                dp[nums[i]] = max(dp[nums[i]], dp[num]+1)
        return max(dp)
                    
                
