"""
special case:
n = 4
offers = [[0,0,5],[3,3,1],[1,2,5],[0,0,7]]

solution:
dp[k] is the maximum gold we can get from selling [0, k) houses.

For dp[k + 1]:
	we get at least the same profit as for dp[k].
	For offers [start, end, gold] with end == k:
		we check if we can get more money from dp[start] + gold.
	To quickly get offers with end == k, we first put them into the map m.
"""
class Solution:
	# TLE: 502/534 passed
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        n = len(offers)
        res = 0
        def backtrack(i, gold, end):
            nonlocal res
            # update max res
            res = max(res, gold)
            if i == n:
                return
            # case 1: do not overlap, sell the houses & update end
            if offers[i][0] > end:
                backtrack(i+1, gold+offers[i][2], offers[i][1])
            # case 2: skip the houses
            backtrack(i+1, gold, end)
        backtrack(0, 0, -1)
        return res
            
            
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # dp[k] = max gold for selling [0,k) houses
        # dp[k+1] = at least dp[k], and get the max dp[start] + gold for offers with same end k
        dp = [0]*(n+1)
        ends = [[] for i in range(n)]
        for s, e, g in offers:
            ends[e].append((s,g))
        for k in range(n):
            dp[k+1] = dp[k]
            for s, g in ends[k]:
                dp[k+1] = max(dp[k+1], dp[s]+g)
        return dp[n]
                
        
                   
            