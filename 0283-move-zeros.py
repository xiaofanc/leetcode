class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                print(i,j,nums[i], nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)    

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                left = i
                right = i + 1
                break
            if i == len(nums)-1:
                return nums
        while right <= len(nums)-1:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums
                    
s=Solution()
print(s.moveZeroes([1,1,0,3,12]))
