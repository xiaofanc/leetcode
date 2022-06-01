"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
Input: nums = [3,4,5,1,2]
Output: 1
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = float('inf')
        while l <= r:
            # sorted
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,1])) # 1
    print(s.findMin([3,4,5,1,2])) # 1