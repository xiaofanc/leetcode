class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            #print(left, mid, right)
            if nums[mid] == target:
                return True
            # cannot decide which side is non-decreasing
            if nums[mid] == nums[right]: 
                right -= 1
            elif nums[mid] < nums[right]:
                # right side is non-decreasing
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # nums[mid] > nums[right]
                # left side if non-decreasing
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            #print(left, mid, right)
        return False       
          

if __name__ == '__main__':
    s = Solution()
    print(s.search([3,5,1], 3)) # True
    print(s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2)) # True
    print(s.search([1,0,1,1,1], 0)) # True