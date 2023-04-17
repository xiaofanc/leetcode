"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: The maximum total we can obtain is 101.
"""

class Solution:
	# 77 / 122 testcases passed
    # check all possible
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        pos = [0 for i in range(len(piles))]
        # max total after choosing k coins with current piles
        dp = {}
        def dfs(k, pos):
            if tuple(pos) in dp:
                return dp[tuple(pos)]
            if k == 0:
                return 0
            res = 0
            # select one element from the current pile
            for i in range(len(piles)):
            	# if current pile is empty
                if pos[i] == len(piles[i]):
                    continue
                cur = piles[i][pos[i]]
                pos[i] += 1
                cur += dfs(k-1, pos)
                res = max(res, cur)
                pos[i] -= 1
            dp[tuple(pos)] = res
            return res
        return dfs(k, pos)

class Solution:
    # Time: O(n*k*l) as n and k are the states and for each recursive call , in worst case we iterate over the entire pile. 
    # Further O(n*k*l) = O(m*k) where m = n*l i.e. m = sum(lens(A[i])) and l = roughly the size of each pile and n = no. of piles and k in worst case can also be m so TC : O(m*m)
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = {}
        # choose k coins from pile[i] to pile[n-1]
        # We can pick 0,1,2,3... elements from the current pile[i] one by one.
        # It asks for the maximum total value of coins we can have, so we need to return max of all the options.
        def dfs(i, k):
            if (i, k) in dp:
                return dp[(i, k)]
            if i == len(piles) or k == 0:
                return 0
            res, cur = dfs(i+1, k), 0
            # select j items from the current pile
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + dfs(i+1, k-j-1))
            dp[(i, k)] = res
            return res
        return dfs(0, k)
            


