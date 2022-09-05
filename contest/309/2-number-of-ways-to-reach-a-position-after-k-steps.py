"""
2400.
"""

class Solution:
	# Time: O(2^k)
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # 1+1+1-1 = 2, 1+1-1+1=2, 1-1+1+1=2
        memo = {}
        def backtrack(i, combs):
            # print("comb->", i, comb, combs)
            if (i, combs) in memo:
                return memo[(i, combs)]
            if i == k and combs == endPos:
                return 1
            if i == k and combs > endPos:
                return 0
            if i > k:
                return 0
            res = 0
            res += backtrack(i+1, combs+1)
            res += backtrack(i+1, combs-1)
            res = res % (10**9+7)
            memo[(i, combs)] = res
            return res
        
        return backtrack(0,startPos)
        

from math import comb
	# Time: O(n choose k)
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # 1+1+1-1 = 2, 1+1-1+1=2, 1-1+1+1=2
        # left + right = k
        # right - left = endPos - startPos
        # right = (endPos - startPos + k) // 2
        if (endPos - startPos + k) % 2 != 0:
            return 0
        right = (endPos - startPos + k) // 2
        # select right items from k items without repetition and without order
        # i.e.5里面选2个为+1，其他为-1
        return comb(k, right) % (10**9+7)      


    # DP - Time: O(l^2)
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # number of ways for k steps and distance d
        # dp[k][d] = dp[k-1][abs(d-1)] + dp[k-1][d+1]
        # we can reach distance k in one way by using k steps: dp[k][k] = 1
        # for step i and distance j, we can reach it in dp[i-1][abs(j-1)] + dp[i-1][j+1] ways
        d = abs(endPos - startPos)
        l = max(k, d)
        dp = [[0 for i in range(l+1)] for j in range(l+1)]
        for i in range(l+1):    # k, if d==k: only one way
            dp[i][i] = 1
            for j in range(i):  # d, if d>k: dp[k][d] = 0
                # reach distance j by one step further
                dp[i][j] = (dp[i-1][abs(j-1)] + dp[i-1][j+1]) % (10**9+7)
        return dp[k][d]



        





