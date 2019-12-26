"""
same as matix multiplication
"""
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)-1
        dp = [[0]*n for _ in range(n)]
        for w in range(1, n):
            for i in range(n-w):
                j = i + w
                maxcost = max(dp[i][l]+dp[l+1][j]+nums[i]*nums[l+1]*nums[j+1] for l in range(i, j))
                dp[i][j] = maxcost
        return dp[0][-1]
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,1,5,8]) == 167)