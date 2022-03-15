"""
LC 209.
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

target = 7, nums = [2,3,1,2,4,3]
output: 2
The subarray [4,3] has the minimal length under the problem constraint.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        s = 0
        minlen = float('inf')
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                minlen = min(minlen, j-i+1)
                s -= nums[i]
                i += 1
        return minlen if minlen != float("inf") else 0

if __name__ == '__main__':
	s = Solution()
	print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
	print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
	print(s.minSubArrayLen(15, [1,2,3,4,5]))
	