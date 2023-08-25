"""
nums: [2,2,3]
k = 0

https://leetcode.com/problems/find-the-longest-equal-subarray/discuss/3938738/python3-o-n-sliding-window-with-better-explanation-for-the-logic-and-edge-cases/

I think the most confusing part, is that:
Since maxf is actually the max frequency in HISTORY (not the current subarray), then why we usej - i + 1 - maxf to determine if the subarray is valid or not? The numbers correspond to maxf may not be even in the subarray!!!

The answer is, the subarray may indeed be invalid, but, it is always guaranteed to be valid when we are updating maxf, namely, when for nums[j] we get count[nums[j]] > maxf, the subarray is valid.
"""
class Solution:
    # TLE: 1413/1421 passed
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        count = collections.Counter()
        res = 0
        # when window length - max count > k: shrink window
        for r in range(len(nums)):
            count[nums[r]] += 1
            if r-l+1 - max(count.values()) > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, max(count.values()))
        return res
            
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        count = collections.Counter()
        maxf = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            maxf = max(maxf, count[nums[r]])

            if r-l+1 - maxf > k:
                count[nums[l]] -= 1
                l += 1
        return maxf
        