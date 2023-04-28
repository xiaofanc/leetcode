"""
Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
Output: [-1,-2,-2]
Explanation: There are 3 subarrays with size k = 3. 
The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1. 
The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2. 
The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.

Input: nums = [-1,-2,-3,-4,-5], k = 2, x = 2
Output: [-1,-2,-3,-4]
Explanation: There are 4 subarrays with size k = 2.
For [-1, -2], the 2nd smallest negative integer is -1.
For [-2, -3], the 2nd smallest negative integer is -2.
For [-3, -4], the 2nd smallest negative integer is -3.
For [-4, -5], the 2nd smallest negative integer is -4. 
"""

import bisect
class Solution:
	# TLE: O(n*n), 708 / 717 testcases passed
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l, r = 0, 0
        res = []
        window = []
        
        while r < len(nums):
            bisect.insort(window, nums[r]) # O(logn) / O(n) in the worst case
            if r-l+1 == k:
                # window is sorted
                if window[x-1] >= 0:
                    res.append(0)
                else:
                    res.append(window[x-1])
                # update window
                window.remove(nums[l]) # O(n)
                l += 1
            r += 1
        return res               
            
    # Time: O(50n), counting sort                     
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # Since the range of numbers is small -50 <= nums[i] <= 50 we can use this to our advantage. Store counts of numbers smaller than 0 in a counter array and use that to find the xth smallest number.
        l = 0
        r = 0
        res = []
        window = [0]*50 # count of neg integers
        
        while r < len(nums):
            if nums[r] < 0:
                window[nums[r]] += 1
            if r - l + 1 == k:
                cnt = 0
                for i in range(50):
                    cnt += window[i]
                    if cnt >= x:
                        res.append(i-50)
                        break
                if cnt < x:
                    res.append(0)
                # shrink the window
                if nums[l] < 0:
                    window[nums[l]] -= 1
                l += 1
            r += 1
        return res  

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = [0] * (len(nums)-k+1)
        window = [0]*50
        for i in range(len(nums)):
            if nums[i] < 0:
                window[nums[i]] += 1
            # shrink the window
            if i >= k and nums[i-k] < 0:
                window[nums[i-k]] -= 1
            if i-k+1 < 0:
                continue
            else:
                # i = k-1
                cnt = 0
                for j in range(50):
                    cnt += window[j]
                    if cnt >= x:
                        res[i-k+1] = j-50
                        break
        return res                

"""
The time complexity of the add method in a SortedList data structure implemented using a balanced binary search tree (such as Red-Black Tree or AVL Tree) is O(log N) in the worst case.
The time complexity of the remove method in a SortedList data structure implemented using a balanced binary search tree (such as Red-Black Tree or AVL Tree) is O(log N) in the worst case.
"""                
from sortedcontainers import SortedList
class Solution:
	# Time: O(nlogk)
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl, ans = SortedList(), []
        for i, y in enumerate(nums):
            sl.add(y)                 # O(logk)
            if len(sl) > k: sl.remove(nums[i - k])  # O(logk)
            if i >= k - 1: ans.append(min(0, sl[x - 1]))
        return ans                
            
        
                
            
        