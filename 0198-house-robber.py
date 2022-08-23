"""
let DP[i] = the maximum money the robber can get from the first i house 
base case:
DP[0] = nums[0]
DP[1] = max(nums[0], nums[1])
recursive rule:
DP[i] = max(DP[i-1], DP[i-2] + nums[i])

[2, 7, 9, 13, 11, 1]
[2, 7, 11,20, 22, 22]

"""


from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            pre, cur = cur, max(nums[i]+pre, cur)
        return cur
    
    def rob2(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return max(nums[0], 0)
        DP = [0] * len(nums)
        DP[0] = max(nums[0], 0)
        DP[1] = max(nums[0], nums[1], 0)
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-2] + nums[i], DP[i-1])
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

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        f1, f2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f1, f2 = f2, max(f1+nums[i], f2)
        return f2

s = Solution()
print(s.rob1([2,7,9,3,1,4,2,8,10]))

            
            