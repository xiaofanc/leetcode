"""
let DP[i] = the maximum money the robber can get from the first i house 
base case:
DP[0] = nums[0]
DP[1] = max(nums[0], nums[1])
recursive rule:
DP[i] = max(DP[i-1], DP[i-2] + nums[i])

Houses are in a loop, if you rob the first house, then you cannot rob the last house
Split into 2 subproblems since we cannot rob the first house and the last house together
Compare max of rob houses[1:] and max of rob houses[:-1]
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            pre, cur = 0, 0
            for n in nums:
                newrob = max(n+pre, cur)
                pre, cur = cur, newrob
            return cur
        
        # edge case: [1]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

    def rob(self, nums: List[int]) -> int:
        maxMoney = 0
        if len(nums) <= 2:
            return max(nums)
        # do not rob the last house
        f1, f2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            f1, f2 = f2, max(f1+nums[i], f2)
        maxMoney = f2
        # do not rob the first house
        f1, f2 = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            f1, f2 = f2, max(f1+nums[i], f2)
        maxMoney = max(maxMoney, f2)
        return maxMoney

    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            res = max(helper(nums[:-2]) + nums[-1], helper(nums[:-1]))
            memo[tuple(nums)] = res
            return res
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        
if __name__ == '__main__':
    s = Solution()
    print(s.rob([1])) # [1]


