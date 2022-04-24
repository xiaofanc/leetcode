"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        numsset = [set(num) for num in nums]
        common = numsset[0]
        for num in numsset[1:]:
            common = common.intersection(num)
        common = sorted(list(common))
        return common

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]