"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

"""


class Solution:
	# TLE
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if prod > 0:
                    res = max(res, j-i+1)
        return res

    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        # the longest subarray with pos/neg product ending with nums[i]
        pos, neg = 0, 0
        for n in nums:
            if n > 0:
                # pos * n = pos
                pos = pos + 1
                # neg * n = neg
                # if no neg in the previous, no chance to get neg prod, neg = 0
                # else neg = neg + 1
                neg = neg + 1 if neg > 0 else 0
            elif n < 0:
                tmp = pos
                # neg * n = pos
                # if no neg in the previous, no chance to get pos prod, pos = 0
                pos = neg + 1 if neg > 0 else 0
                # pos * n = neg
                neg = tmp + 1
            else:
                pos, neg = 0, 0
            res = max(res, pos)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.getMaxLen([-1,-2,-3,0,1])) # 2


                
                

                