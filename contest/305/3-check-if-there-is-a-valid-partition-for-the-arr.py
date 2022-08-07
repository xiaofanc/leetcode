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
            res = False
            # condition-1
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                res = res or solve(i+2)
                # condition-2
                if i+2 < len(nums) and nums[i] == nums[i+2]:
                    res = res or solve(i+3)
            # condition-3
            if i+2 < len(nums) and nums[i+1] - nums[i] == 1 and nums[i+2] - nums[i+1] == 1:
                res = res or solve(i+3)
            dp[i] = res
            return res

        return solve(0)

    def validPartition(self, nums: List[int]) -> bool:
        # dp[i] = if nums[i:] can be partitioned into valid subarrays
        n = len(nums)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n-1,-1,-1):
            # condition-1
            if i < n-1 and nums[i] == nums[i+1] and dp[i+2]:
                dp[i] = True
                continue
            # condition-2
            if i < n-2 and nums[i] == nums[i+1] == nums[i+2] and dp[i+3]:
                dp[i] = True
                continue
            # condition-3
            if i < n-2 and nums[i+1]-nums[i] == 1 and nums[i+2]-nums[i+1] == 1 and dp[i+3]:
                dp[i] = True
        return dp[0]

    def validPartition(self, nums: List[int]) -> bool:
        # dp[i] = if nums[:i+1] can be partitioned into valid subarrays
        n = len(nums)
        dp = [False] * (n)
        if n <= 1:
            return False
        
        if nums[0] == nums[1]:
            dp[1] = True
        if n == 2: return dp[1]
        
        if nums[0] == nums[1] == nums[2]:
            dp[2] = True
        if nums[1]-nums[0] == 1 and nums[2]-nums[1] == 1:
            dp[2] = True
        if n == 3: return dp[2]
        
        for i in range(3, n):
            if nums[i] == nums[i-1] and dp[i-2]:
                dp[i] = True
            if nums[i] == nums[i-1] == nums[i-2] and dp[i-3]:
                dp[i] = True
            if nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[i-3]:
                dp[i] = True
        return dp[-1]

if __name__ == '__main__':
     s = Solution()
     print(s.validPartition([1,2])) 
     print(s.validPartition([2,2]))                    # True
     print(s.validPartition([473928,473929,473930]))   # True
     print(s.validPartition([4,4,4,5,6]))              # True

            
                
