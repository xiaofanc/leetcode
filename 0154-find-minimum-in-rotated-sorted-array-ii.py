"""
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
Input: nums = [2,2,2,0,1]
Output: 0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r: # or l < r
            
            mid = l + (r-l)//2
            # print(l, mid, r)
            if nums[mid] == nums[r]:
                r -= 1
            # right side is non-decreasing, search left part
            elif nums[mid] < nums[r]:
                r = mid
            # left side is non-decreasing, search right part
            else:
                l = mid + 1
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            
            m = (l+r) // 2
            if nums[m] == nums[l]:
                l += 1
            elif nums[m] > nums[l]: # left is sorted
                l = m + 1
            else:
                r = m
        return nums[m]
        
if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,2,2,0,1]))
    print(s.findMin([1,3,5]))                