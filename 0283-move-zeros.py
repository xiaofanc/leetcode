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
            
s=Solution()
print(s.moveZeroes([1,1,0,3,12]))
