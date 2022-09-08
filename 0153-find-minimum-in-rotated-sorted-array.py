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
            # if left to right is sorted or only 1 num left
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == nums[r]:
                r -= 1
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]: # why =? [1],[2,1]
                return nums[l]
            m = l + (r-l) // 2
            # if left is sorted, seach min in the right
            # why no =? since only when l=r=m, m=r, it is handled before (if nums[l] <= nums[r])
            if nums[m] > nums[r]: 
                l = m + 1
            else: # seach min in the left
                r = m
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            if nums[l] <= nums[r]:  # why =? : [1],[2,1]
                return nums[l]
            m = l + (r-l) // 2
            # print("m", m, l, r)
            # if left is sorted, seach min in the right
            # why =? since l to r is not sorted, therefore when m == l, we need to search from m+1
            if nums[m] >= nums[l]: 
                l = m + 1
            else: # seach min in the left, possible m is the min num
                r = m
        return nums[r] # does not matter


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,1])) # 1 why must l <= r and nums[m] >= nums[l]
    print(s.findMin([3,1,2])) # 1
    print(s.findMin([3,4,5,1,2])) # 1


