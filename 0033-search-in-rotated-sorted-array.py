"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

class Solution: 
    # one pass solution
    # compare with middle and end to find out which part to search
    def search(self, nums: List[int], target: int) -> int:
        # modified binary search
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2
            # stop point
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[end]: #right part of mid is sorted
                if target > nums[end] and target < nums[mid]:
                    end = mid - 1
                else: # target > nums[mid] or target <= nums[end]
                    start = mid + 1
            else: # left side of mid is sorted
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # find the sorted window
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        # find the index of the smallest value using binary search.
        def find_pivot_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right)//2
                #print(pivot)
                if nums[pivot] > nums[pivot+1]:
                    return pivot + 1 # pivot index
                elif nums[pivot] > nums[left]: # search right part
                    left = pivot
                else: # search left part
                    right = pivot   # could be a problem in second case if right = pivot - 1
        
        def search(left, right):
            """
            already find the left/right part of pivot to search
            subarray is in ascending order
            binary search for the target
            """
            while left <= right:
                pivot = (left + right)//2
                if nums[pivot] == target:
                    return pivot
                elif nums[pivot] > target:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1
        
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        pivot_index = find_pivot_index(0, n-1)
        #print(pivot_index)
        if nums[pivot_index] == target:
            return pivot_index
        elif pivot_index == 0: # not rotated
            return search(0, n-1)
        elif target >= nums[0]: # search left part of pivot
            return search(0, pivot_index)
        else: # search right part of pivot
            return search(pivot_index, n-1)              

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        
        def helper(nums, target, l, r):
            if l > r:
                return -1
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: # left is sorted
                if nums[l] <= target and target < nums[mid]:
                    return helper(nums, target, l, mid-1)
                else:
                    return helper(nums, target, mid+1, r)
            else: # right is sorted
                if nums[mid] < target and target <= nums[r]:
                    return helper(nums, target, mid+1, r)
                else:
                    return helper(nums, target, l, mid-1)
                
        return helper(nums, target, low, high)                    

if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
    print(s.search([4,5,1,2,3], 1))

         
                    
        
            
            
            
        
        