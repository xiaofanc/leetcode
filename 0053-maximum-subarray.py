"""
have to choose a number;

running sum is the maximum subarray at each point
Calculate the running sum by using a for-loop
During each for-loop, we compare the number with running sum. If after adding the 
number, the running sum is less than the current number, then we will reset running 
sum as current number (not 0). At the same time, we will also update the maxsum by 
comparing it with the cursum

       [-2, 1, -3, 4, -1, 2, 1, -5, 4]
cursum [-2, 1, -2, 4,  3, 5, 6,  1, 5]
maxsum [-2, 1,  1, 4,  4, 5, 6,  6, 6]

"""
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = nums[0]
        for i in range(1,n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum) 
        
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = nums[0]
        for i in range(1,len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(cursum, maxsum)
        return maxsum
    
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, ans = nums[0]
        for i in range(1, len(nums)):
            cursum = nums[i] + max(0, cursum)
            ans = max(cursum, ans)
        return ans
    
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = 0, nums[0]
        for n in nums:
            cursum = max(cursum + n, n)
            maxsum = max(cursum, maxsum)
            print(cursum, maxsum)
        return maxsum

    def maxsub(nums):
        dp, ans = 0, 0
        for i in range(len(nums)):
            dp = nums[i] + max(0, dp) # the max sum obtained from beginning to num[i-1] which includes num[i-1]
            ans = max(ans, dp)        # the max sum for any substring
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        dp, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            dp = max(dp, 0) + n
            maxsum = max(maxsum, dp)
        return maxsum
        
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
