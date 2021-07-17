class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r: # or l < r
            
            mid = l + (r-l)//2
            # print(l, mid, r)
            if nums[mid] == nums[r]:
                r -= 1
            # right side is non-decreasing
            elif nums[mid] < nums[r]:
                r = mid
            # left side is non-decreasing
            else:
                l = mid + 1
        return nums[l]

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,2,2,0,1]))
    print(s.findMin([1,3,5]))                