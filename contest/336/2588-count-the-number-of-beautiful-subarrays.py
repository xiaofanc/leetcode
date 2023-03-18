"""
# 0560

nums[i] XOR nums[j] equals to apply the operation in all possible bits then sum it.
For example:
[3, 1, 2] (in binary [0011, 0001, 0010])

Step1:
Normal way:
Choose [3, 1, 2] and k = 1. Subtract pow(2, 1) from both numbers. The subarray becomes [1, 1, 0].
XOR way:
3 ^ 2 = 1 (0011 ^ 0010 = 0001) . The subarray becomes [1, 1]. The difference is we sum two numbers.

Step2:
Normal way:
Choose [1, 1, 0] and k = 0. Subtract pow(2, 0) from both numbers. The subarray becomes [0, 0, 0].
XOR way:
1 ^ 1 = 0 (0001 ^ 0001 = 0000) . The subarray becomes [0].

The array contains non negative numbers, therefore all elements are zeros if the sum of array is zero.
"""


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # count the number of subarray which makes XOR of all elements = 0
        # 1 ^ 1 = 0, 1 ^ 1 ^ 1 = 1
        prefixXor = Counter({0:1})
        s = 0
        res = 0
        for num in nums:
            s ^= num
            # s^s = 0, the xor of numbers between i and j = 0
            # prefixXor[s] represents how many subarrays before have XOR == s
            res += prefixXor[s] 
            prefixXor[s] += 1
        return res



