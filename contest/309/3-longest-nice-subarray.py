"""
2401.
"""

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        for i in range(1,len(nums)):
            n = nums[i]
            l = 1
            for j in range(i-1,-1,-1):
                if n & nums[j] == 0:
                    n = n|nums[j]
                    l += 1
                    res = max(res, l)
                else:
                    break
        return res
                    
    # sliding window: O(N)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        n = 0
        res = 1
        for r in range(len(nums)):
            # shrink the window until no conflicts
            # xor return 1 if bit is different
            while n & nums[r] != 0:
                n = n ^ nums[l]  # remove nums[l]
                l += 1
            n = n | nums[r]  # include nums[r]
            res = max(res, r-l+1)
        return res