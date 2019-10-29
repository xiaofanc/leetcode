from typing import List
class Solution:
    def rotate0(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        return nums
        
    def rotate1(self, nums, k):
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k] 
            return nums
        
    def rotate2(self, nums: List[int], k: int) -> None:
        def numsreverse(start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
            return nums
        k, n = k % len(nums), len(nums)
        if k:
            numsreverse(0,n-1)
            numsreverse(0,k-1)
            numsreverse(k,n-1)
        return nums
        
        
        
s=Solution()
print(s.rotate0([1,2,3,4,5,6,7],3))
print(s.rotate1([-1,-100,3,99],2))
print(s.rotate2([-1,2],3))
print(s.rotate2([-1,2],4))

