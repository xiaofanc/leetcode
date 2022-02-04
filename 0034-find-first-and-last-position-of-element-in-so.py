class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                # mid = target
                l = r = mid
                while l >= 0 and nums[l] == target:
                    l -= 1
                while r <= len(nums)-1 and nums[r] == target:
                    r += 1
                return [l+1, r-1]
        return [-1, -1]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]

"""
    [5,7,8,8,8,10], 8
    [5,8,8,8,8,10], 8
"""

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            if nums[mid] == target:
                
                if isFirst:
                    print('left: ')
                    print(begin, mid, end)  # 0, 2, 5
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    print('right: ')
                    print(begin, mid, end)
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = higher = -1
        
        def searchLowerBound(nums, target, low, high):
            if low > high:
                return -1
            middle = low + (high-low)//2
            if nums[middle] == target and (middle == 0 or nums[middle-1] < target):
                return middle
            if target <= nums[middle]:
                return searchLowerBound(nums, target, low, middle-1)
            else:
                return searchLowerBound(nums, target, middle+1, high)

        def searchHigherBound(nums, target, low, high):
            if low > high:
                return -1
            middle = low + (high-low)//2
            if nums[middle] == target and (middle == len(nums)-1 or nums[middle+1] > target):
                return middle
            if target < nums[middle]:
                return searchHigherBound(nums, target, low, middle-1)
            else:
                return searchHigherBound(nums, target, middle+1, high)
        
        lower = searchLowerBound(nums, target, 0, len(nums)-1)
        higher = searchHigherBound(nums, target, 0, len(nums)-1)
        return [lower, higher]
        
if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([1], 1)) # [0,0]
    print(s.searchRange([5,7,7,8,8,10], 8)) # [3,4]



    