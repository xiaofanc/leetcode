"""
You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].

It is guaranteed that in the ith operation:

operations[i][0] exists in nums.
operations[i][1] does not exist in nums.

Input: nums = [1,2], operations = [[1,3],[2,1],[3,2]]
Output: [2,1]
Explanation: We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [3,2].
- Replace the number 2 with 1. nums becomes [3,1].
- Replace the number 3 with 2. nums becomes [2,1].
We return the array [2,1].

"""

class Solution:
	# TLE
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
    	
        for oper in operations:
            for i in range(len(nums)):
                if nums[i] == oper[0]:
                    nums[i] = oper[1]
        return nums

    # use hashmap to record index of each number
    # update hashmap after replacing
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexMap = {}
        for i, n in enumerate(nums):
            indexMap[n] = i
        for oper in operations:
            idx = indexMap[oper[0]]
            nums[idx] = oper[1]
            del indexMap[oper[0]]
            indexMap[oper[1]] = idx
        return nums                    



        