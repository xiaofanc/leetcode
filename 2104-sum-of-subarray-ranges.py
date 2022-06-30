"""
Return the sum of all subarray ranges of nums.

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

# 先看907
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            minInt, maxInt = nums[i], nums[i]
            for j in range(i, len(nums)):
                if nums[j] > maxInt:
                    maxInt = nums[j]
                if nums[j] < minInt:
                    minInt = nums[j]
                res += maxInt - minInt
        return res

    # monotonic stack
    def subArrayRanges(self, nums: List[int]) -> int:
        nums1 = [float("-inf")] + nums
        # store the sum of minvalues for subarrays that end with nums[i]
        minSum = [0] * len(nums1)
        stack = [0]
        for i in range(1, len(nums1)):
            # find the first num nums1[j] <= nums1[i]
            while nums1[stack[-1]] > nums1[i]:
                stack.pop()
            j = stack[-1]
            minSum[i] = minSum[j] + nums1[i] * (i-j)
            stack.append(i)
        
        nums2 = [float("inf")] + nums
        # store the sum of maxvalues for subarrays that end with nums[i]
        maxSum = [0] * len(nums2)
        stack = [0]
        for i in range(1, len(nums2)):
        	# find the first prev num >= nums2[i]
            while nums2[stack[-1]] < nums2[i]:
                stack.pop()
            j = stack[-1]
            maxSum[i] = maxSum[j] + nums2[i] * (i-j)
            stack.append(i)
        # print(maxSum, minSum)
        return sum(maxSum) - sum(minSum)
        
if __name__ == '__main__':
	s = Solution()
	print(s.subArrayRanges([1,2,3]))  # 4
