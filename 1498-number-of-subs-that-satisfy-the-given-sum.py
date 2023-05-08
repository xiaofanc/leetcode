"""
If there are k subsequences with min as the minimum value and max as the maximum value, we only need to check if min + max <= target. The number of such subsequences k depends on how many elements have values that are between min and max. Therefore, we need to sort nums first, so that the number of values between min and max can be represented by their index difference.

For each number in the range [left + 1, right], there are 2 options: we can either take it or not take it, so there are a total of 2^{right - left} valid subsequences that have nums[left] as the minimum element.

find the right for the largest element which is smaller than or equal to target - nums[left]
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] + nums[r] <= target:
            	# nums[l] nust include in the subseq
                # we can freely pick elements within the range [left + 1, right] to make valid subsequences
                res += 2**(r-l)
                res %= 10**9+7
                l += 1
            else:
                r -= 1
        return res

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9+7
        
        for l in range(len(nums)):
            # bisect_right find the first number > target-nums[l]
            r = bisect.bisect_right(nums, target-nums[l])-1
            if r >= l:
                res += pow(2, r-l, mod)
        return res % mod

