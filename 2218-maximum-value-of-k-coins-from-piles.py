"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: The maximum total we can obtain is 101.
"""

class Solution:
	# 77 / 122 testcases passed
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        pos = [0 for i in range(len(piles))]
        # max total after choosing k coins with current piles
        dp = {}
        def dfs(k, pos):
            if tuple(pos+[k]) in dp:
                return dp[tuple(pos+[k])]
            if k == 0:
                return 0
            res = 0
            for i in range(len(piles)):
            	# if current pile is empty
                if pos[i] == len(piles[i]):
                    continue
                cur = piles[i][pos[i]]
                pos[i] += 1
                cur += dfs(k-1, pos)
                res = max(res, cur)
                pos[i] -= 1
            dp[tuple(pos+[k])] = res
            return res
        return dfs(k, pos)
