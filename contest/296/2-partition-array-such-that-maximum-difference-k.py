"""
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.

Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Input: nums = [3,6,1,2,5], k = 2
Output: 2
Explanation:
We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.
"""

class Solution:
	# [16,8,17,0,3,17,8,20] did not pass
	# [16,8,17,17], [0,3,8], [20] using this method
	# However, [16,17,17,20], [0,3,8,8] is the answer
	# 直接partition行不通
    def partitionArray(self, nums: List[int], k: int) -> int:
        res = [[nums[0]]]
        for n in nums[1:]:
            i = 0
            while i < len(res):
                lst = res[i]
                if max(lst)-k <= n <= min(lst)+k:
                    lst.append(n)
                    break
                else:
                    i += 1
            if i == len(res):
                res.append([n])
        return len(res)

    # sort一下，求是否 n-minval <= k
    # subsequence does not matter
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        minval = nums[0]
        for n in nums:
            if n-minval <= k:
                continue
            else:
                minval = n
                res += 1
        return res
                

        