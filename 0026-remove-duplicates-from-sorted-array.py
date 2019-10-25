from typing import List
class Solution:
    def removeDuplicates0(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                 del nums[i]
            else:
                i += 1
        print(nums)
        return len(nums)

    
    def removeDuplicates1(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        #del nums[slow+1:] 
        print(nums)
        return slow+1
    
    def removeDuplicates2(self, nums: List[int]) -> int:   
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        print(nums)
        return len_
        
  
            
s=Solution()
print(s.removeDuplicates0([1,2,2,3,4,4,5,5,6]))
print(s.removeDuplicates1([1,2,2,3,4,4,5,5,6]))
print(s.removeDuplicates2([1,2,2,3,4,4,5,5,6]))