"""
6137.
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
"""

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        def solve(i):
            if i == len(nums):
                return True
            if i > len(nums):
                return False
            if dp[i] != -1:
                return dp[i]
            # condition-1
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                if solve(i+2): 
                    return True
                # condition-2
                if i+2 < len(nums) and nums[i] == nums[i+2]:
                    if solve(i+3): 
                        return True
            # condition-3
            if i+2 < len(nums) and nums[i+1] - nums[i] == 1 and nums[i+2] - nums[i+1] == 1:
                if solve(i+3): 
                    return True
            dp[i] = False
            return dp[i]
        
        return solve(0)
        
            
                
