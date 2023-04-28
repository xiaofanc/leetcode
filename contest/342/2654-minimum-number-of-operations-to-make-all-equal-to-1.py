"""
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

Approach
The key is to find at least one 1 in th the nums, once found then other can be made 1 with n -1 operations.
To have least no. of operations we need to find the smallest subarray whose gcd is 1.
For this, with greedy approach we will check each sub array and evaluate gcd and keep storing the minimum length for which GCD is 1.
Corner case : if there is already x no. of 1s in the array, then simply needed n-x no of operation.

Therefore:
If there is one in the nums: res = len(nums)-count(1)
If there is not one in the nume:
- find the smallest subarray whose gcd is 1
- number of operations to make nums[i] = 1: j-i when gcd(nums[i:j+1]) = 1
	-> [16,24,36,54,81] to take min operations to get a one, replace the nums in reverse order
	-> [16,24,36,27,81]
	-> [16,24,9 ,27,81]
	-> [16,3 ,9 ,27,81]
	-> [1 ,3 ,9 ,27,81]
- number of operations to make the left numbers = 1: len(nums)-1

Q3. How do you get the minimum number of operations required to make any of the elements as 1?
A3. given the constraints, for any element I we can traverse through all elements (say iterator j) from i+1 to n and take their gcd. As soon as the gcd becomes 1 we can conclude that taking gcd in the reverse fashion (from nums[j] to nums[i]) would make nums[i] equal to 1.
"""

import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones:
            return len(nums)-ones
        # if there is no one in the nums, find the smallest subarray with
        # gcd = 1 to create a one, min operations = j-i
        diff = float('inf')
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i+1, len(nums)):
                g = math.gcd(g, nums[j])
                if g == 1:
                    diff = min(diff, j-i)
        return -1 if diff == float('inf') else diff + len(nums) - 1











