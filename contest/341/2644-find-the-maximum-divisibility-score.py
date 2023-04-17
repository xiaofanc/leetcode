"""
You are given two 0-indexed integer arrays nums and divisors.
The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].
Return the integer divisors[i] with the maximum divisibility score. If there is more than one integer with the maximum score, return the minimum of them.
"""

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxs, maxd = -1, None
        for d in divisors:
            c = 0
            for n in nums:
                if n % d == 0:
                    c += 1
            if c > maxs:
                maxs = c
                maxd = d
            elif c == maxs:
                maxd = min(maxd, d)
        return maxd
        
        