"""
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
"""

class Solution:
	# TLE: 50 / 1061 testcases passed
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        dct = set()
        n = len(nums)
        for i in range(len(nums)):
            # print("nums[i]: ", nums[i])
            updated = False
            while nums[i] < 0:
                nums[i] += value
                while nums[i] in dct:
                    nums[i] += value
                updated = True
            while not updated: # nums >= 0
                # add smaller integer first
                for target in range(n):
                    if (nums[i] - target) % value == 0 and target not in dct:
                        nums[i] = target
                        break
                updated = True
            dct.add(nums[i])
            # print("dct ", dct)
        for i in range(n):
            if i not in dct:
                return i
        return n
                    
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
    	# n % value is the minimum non-negative value we can achieve

        m = Counter([n % value for n in nums])
        for i in range(len(nums)):
            if m[i % value] == 0:
                return i
            # different i can have same i % value, 0 % 5 == 5 % 5, count mod == 0 in the nums
            m[i % value] -= 1
        return len(nums)






