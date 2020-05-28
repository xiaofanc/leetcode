"""
subarray can be empty!

Calculate the running sum by using a for-loop
During the for-loop, add number into the running sum, if the running sum is less 
than 0, then we restart (which means we set it as 0, not choosing a number). 
For each loop, we will also update the maxsum by comparing it with the cursum

       [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cursum [ 0, 1,  0, 4,  3, 5, 6,  1, 5]
maxsum [ 0, 1,  1, 4,  4, 5, 6,  6, 6]

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = 0
        for n in nums:
            cursum += n
            if cursum < 0:
                cursum = 0
            if cursum > maxsum:
                maxsum = cursum
        return maxsum

    def maxSubArray(self, nums: List[int]) -> int:
        dp = maxsum = 0
        for n in nums:
            dp = max(n, dp+n)   # if dp<0 then restart
            maxsum = max(maxsum, dp)
        return maxsum
        

            
