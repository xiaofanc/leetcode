"""
split nums into 2 subsets with equal sum
solution: check if exists sum(subset) == target

# 0698. canPartitionKSubsets
"""

class Solution:
    # TLE
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)/2
        def backtracking(i, s):
            # print("s", s)
            if s == target:
                return True
            if s > target:
                return
            for j in range(i, len(nums)):
                s += nums[i]
                if backtracking(j+1, s): 
                    return True
                s -= nums[i]
        res = backtracking(0, 0)
        return True if res else False

	# DP
	# Time: O(n*sum(nums)), space: O(sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)/2 != sum(nums)//2:
            return False
        target = sum(nums)/2
        dp = set() # store subset sum
        dp.add(0)
        for n in nums:
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t+n)
                if target in nextDP:
                    return True
            dp = nextDP
        return False

    # Time: O(mxn), where n be the number of array elements and m be the target
    # Top-down DP
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)/2
        nums.sort(reverse = True)
        memo = {}
        def dfs(i, s):
            # if there is subsets from nums[i:] to make up to s
            if s == 0:
                return True
            if s < 0 or i == len(nums):
                return False
            if (i, s) in memo:
                return memo[(i, s)]
            # if no memoization: Time is O(2^n)
            res = dfs(i+1, s-nums[i]) or dfs(i+1, s)
            memo[(i, s)] = res
            return res

        return dfs(0, target)


    # Time: O(mxn), where n be the number of array elements and m be the target
    # Bottom-up DP
    def canPartition(self, nums: List[int]) -> bool:
    # dp[i][j] = if the sum j can be formed by elements in nums[:i]
    # dp[i][j] = True if dp[i-1][j] == True (no need to use nums[i]) or dp[i-1][j-nums[i]] == True
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        n = len(nums)
        
        dp = [[False] * (target+1) for i in range(n+1)]

        dp[0][0] = True
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(target+1):
                if j >= curr:
                    dp[i][j] = dp[i-1][j-curr] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]

    # Time: O(mxn), where n be the number of array elements and m be the target
    def canPartition(self, nums: List[int]) -> bool:
    # dp[j] = if the sum j can be formed by elements
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        n = len(nums)
        
        dp = [False] * (target+1)
        dp[0] = True

        for curr in nums:
            for j in range(target, curr-1, -1): # why start from backwards?
                dp[j] = dp[j] or dp[j-curr]
        return dp[target]

if __name__ == '__main__':
	s = Solution()
	print(s.canPartition([1,2,3,5])) # False
	print(s.canPartition([1,5,11,5])) # True





            
