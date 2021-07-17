class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r: 
            mid = l + (r - l) // 2
            if nums[mid] == nums[mid-1]:
                if (mid-1) % 2 == 0: # check the right window
                    l = mid + 1
                else:
                    r = mid - 2
            elif nums[mid] == nums[mid+1]:
                if (mid) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                return nums[mid]
        return nums[l]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  #2
    print(s.singleNonDuplicate([3,3,7,7,10,11,11]))  #10
