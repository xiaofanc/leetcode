from itertools import accumulate
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # if len(nums) < 3:
            # return 0
        dp = [0]*len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        res = list(accumulate(dp))
        return res[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,4])) # 3
    # [1, 2, 3], [2, 3, 4] and [1,2,3,4]