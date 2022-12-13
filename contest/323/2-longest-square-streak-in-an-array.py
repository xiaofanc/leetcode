"""
Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        dp = [1]*len(nums)
        # print("nums", nums)
        visited = dict()
        for i in range(len(nums)):
            visited[nums[i]]= i
            if math.sqrt(nums[i]) != int(math.sqrt(nums[i])):
                continue
            root = int(math.sqrt(nums[i]))
            if root in visited:
                dp[i] = max(dp[i], dp[visited[root]]+1)
        maxl = max(dp)
        if maxl == 1:
            return -1
        return maxl