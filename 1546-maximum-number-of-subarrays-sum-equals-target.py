"""
Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.
"""

class Solution:
    # variant of two-sum
    # Time: O(n), Space: O(n)
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        lookup = set([0])
        running_sum = 0
        count = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - target in lookup:
                count += 1
                lookup = set() # non-overlapping subsets
            lookup.add(running_sum)
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.maxNonOverlapping([-5,5,-4,5,4], 5)) # 2
    print(s.maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10)) # 3