
class Solution:
	# TLE: O(n^2)
    def minOpenrations(self, nums: List[int], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            opers = 0
            for n in nums:
                opers += abs(q-n)
            res[i] = opers
        return res

"""
We sort our array first, so we can find index i of first element larger than q.

Then, we use the prefix sum array to get:

sum of smaller elements ps[i].
sum of larger elements ps[-1] - ps[i].
The number of operations is:

q * i - ps[i] for smaller elements.
ps[-1] - ps[i] - q * (n - i) for larger elements.
"""
	# O(nlogn)
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ps, n = [0] + list(accumulate(nums)), len(nums)
        res = [0] * len(queries)
        for i, q in enumerate(queries):
            # first number >= q
            idx = bisect_left(nums, q)
            # sum of smaller elements ps[i]
            res[i] += q * idx - ps[idx]
            # sum of larger elements ps[-1] - ps[i]
            res[i] += ps[-1]-ps[idx] - q * (n-idx)
        return res


