"""
find the position of the first number >= target
"""
from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        count = 0
        while l <= r:
            mid = (l + r) // 2
            count += 1
            if count == 30:
                return
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid +1
        return l # the first number that larger than target

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        # find the first number that larger than or equal to the target
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        # loop will stop at the moment when right < left 
        # and nums[right] < target < nums[left]
        # therefore, the proper position to insert the target is at the index left
        return left     
        
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))