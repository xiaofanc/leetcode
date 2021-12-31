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
    
    # Time: O(n)
    def rotate2(self, nums: List[int], k: int) -> None:
        def numsreverse(start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
            return nums
            
        k, n = k % len(nums), len(nums)
        if k:
            numsreverse(0,n-1)  # [7, 6, 5, 4, 3, 2, 1]
            numsreverse(0,k-1)  # [5, 6, 7, 4, 3, 2, 1]
            numsreverse(k,n-1)  # [5, 6, 7, 1, 2, 3, 4]
        return nums
    
    # Time: O(n)
    def rotate3(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i+k) % n] = nums[i] # a[3] = nums[0] = 1
        nums[:] = a
        return nums

    # Time: O(n * k)
    def rotate4(self, nums, k):
        # brute force
        n = len(nums)
        k = k % n
        for i in range(k):
            previous = nums[-1]
            # for each k, rotate the whole nums
            for j in range(n):
                nums[j], previous = previous, nums[j]
        return nums

        
s=Solution()
print(s.rotate0([1,2,3,4,5,6,7],3))
print(s.rotate1([-1,-100,3,99],2))
print(s.rotate2([-1,2],3))
print(s.rotate2([-1,2],4))

