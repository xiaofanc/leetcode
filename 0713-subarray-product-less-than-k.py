"""
I was SO close to solving this via sliding window, but couldn't come up with ans += right - left + 1....

For those who are confused, let's use the example nums = [10,5,2,6]:

If we start at the 0th index, [10,5,2,6], the number of intervals is obviously 1.
If we move to the 1st index, the window is now [10,5,2,6]. The new intervals created are [5] and [10,5], so we add 2.
Now, expand the window to the 2nd index: [10,5,2,6]. The new intervals are [2], [5,2], and [10,5,2], so we add 3.
The pattern should be obvious by now; we add right - left + 1 to the output variable every loop!
"""
class Solution:
    # TLE
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if prod < k:
                    res += 1
                else:
                    break
        return res

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: # n in nums >= 1
            return 0
        # sliding window is only valid since num is positive
        l = r = 0
        prod = 1
        res = 0
        while r < len(nums):
            prod *= nums[r]
            while l < len(nums) and prod >= k:
                prod = prod // nums[l]
                l += 1
            # add r-l+1 subarrays ending with nums[r] each time because the element pointed by the "right" is the new one we are investigating
            # l cannot be out of bound
            if r >= l:
                res += r-l+1
            r += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([1,1,1], 1)) # 0

