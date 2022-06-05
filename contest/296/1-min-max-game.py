"""
Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.

Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.

"""

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = [0] * (len(nums)//2)
            for i in range(len(nums)//2):
                if i % 2:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
                else:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            nums = newNums
        return nums[0]
                
            
            