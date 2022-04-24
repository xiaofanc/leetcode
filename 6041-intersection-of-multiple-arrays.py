"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numsset = [set(num) for num in nums]
        common = numsset[0]
        for num in numsset[1:]:
            common = common.intersection(num)
        common = sorted(list(common))
        return common