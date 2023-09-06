"""
similar: https://leetcode.com/problems/subarray-sums-divisible-by-k/
Current we have acc elements of A[i] % mod == k,
We want to find the prefix subarray where have acc - k elements of A[i] % mod == k.
The diff array has k elements of A[i] % mod == k.
"""

class Solution:
	# TLE: 609/617 passed
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] % modulo

        res = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] == k:
                    cnt += 1
                if cnt % modulo == k:
                    res += 1
        return res
                
class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        res = acc = 0
        count = Counter({0: 1})
        for a in nums:
            acc = (acc + (1 if a % mod == k else 0)) % mod
            res += count[(acc - k) % mod]
            count[acc] += 1
        return res



        
