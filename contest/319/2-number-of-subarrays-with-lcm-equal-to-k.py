"""
Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6], [6], [6,2], [3,6,2]


Input: nums = [5,1,1,1,2], k = 1
Output: 6
Explanation: The subarrays of nums where 1 is the least common multiple of all the subarray's elements are:
- [1xx], [1,1,x], [1,1,1], [x1x], [x,1,1], [xx1]
"""

class Solution:
    def subarrayLCM(self, nums, k):
        res = 0
        def computeGCD(x, y):
            if x == 0:
                return y
            return computeGCD(y % x, x)

        # find the least common multiple of two numbers
        # findLCM(4, 6) = 12 = 4*6//2
        def findLCM(x, y):
            hcf = computeGCD(x, y)
            lcm = (x*y)//hcf
            return lcm

        for i in range(len(nums)):
            currLcm = nums[i]
            for j in range(i, len(nums)):
                currLcm = findLCM(currLcm, nums[j])
                if currLcm == k:  # [1], [1,1], [1,1,1], [x,1], [x,1,1], [x,x,1]
                    res += 1
                elif currLcm > k: # [3,1,6,7], 6 -> [3,1,6], [1,6], [6]
                    break
        return res
           

if __name__ == '__main__':
	s = Solution()
	print(s.subarrayLCM([5,1,1,1,2], 1)) # 6
	print(s.subarrayLCM([3,6,2,7,1], 6)) # 4
	print(s.subarrayLCM([3,1,6,7,1], 6)) # 3
                
                    
