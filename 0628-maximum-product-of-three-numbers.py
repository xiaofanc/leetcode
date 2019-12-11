from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
        
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n < min2:
                if n < min1:
                    min1, min2 = n, min1
                else:
                    min2 = n
                    
            if n > max3:
                if n > max1:
                    max3, max2, max1 = max2, max1, n
                elif n > max2:
                    max3, max2 = max2, n
                else:
                    max3 = n

        return max(min1*min2*max1, max1*max2*max3)
                
    def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
    
    def maximumProduct(self, nums):
        return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])

if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([2,4,1,-3]))
    print(s.maximumProduct([12,4,-1,-5]))
    print(s.maximumProduct([2,78,1,2]))