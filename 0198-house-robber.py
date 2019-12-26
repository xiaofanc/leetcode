from typing import List
class Solution:
    def rob1(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return max(nums[0], 0)
        prev2 = max(nums[0], 0)
        prev1 = max(nums[0], nums[1], 0)
        curr = prev1
        for i in range(2, len(nums)):
            curr = max(prev1, prev2+nums[i])
            prev2, prev1 = prev1, curr
        return curr 
    
    def rob2(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return max(nums[0], 0)
        DP = [0] * len(nums)
        DP[0] = max(nums[0], 0)
        DP[1] = max(nums[0], nums[1], 0)
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-2] + nums[i], DP[i-1])
            print(DP)
        return DP[-1]
            

    def rob3(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return max(nums[0], 0)
        DP = []
        DP.append(max(nums[0], 0))
        DP.append(max(nums[0], nums[1], 0))
        for i in range(2, len(nums)):
            DP.append(max(DP[i-2] + nums[i], DP[i-1]))
            print(DP)
        return DP[-1]

    # recursion:
    def dp(i):
        if i == 0: return max(0, nums[0])
        if i == 1: return max(0, nums[0], nums[1])

        return max(dp(i-2) + nums[i], dp(i-1))
    return dp(len(nums)-1)


    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        # f(k) = max(f(k – 2) + Ak, f(k – 1)) from f(1)
        f = [0] * len(nums)
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            f[i] = max(f[i-2] + nums[i], f[i-1])
            print(f[i-2], f[i-1], f[i])
        return f[-1]

s = Solution()
print(s.rob1([2,7,9,3,1,4,2,8,10]))

            
            