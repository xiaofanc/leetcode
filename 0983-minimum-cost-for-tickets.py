"""
minimum cost to buy tickets to cover the days.
DP: recursion with caching
"""

class Solution:
    # Time: O(n)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i): # minimum cost for tickets start from days[i]
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float("inf")
            for d, c in zip([1,7,30], costs):
                # find the next day needs to cover
                j = i
                while j < len(days) and days[j] < days[i]+d:
                    j += 1
                dp[i] = min(dp[i], c+dfs(j))
            return dp[i]
        return dfs(0)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i] = minimum cost for tickets ends with day i
        extends = [1,7,30]
        dp = [0] * (days[-1]+1)
        
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1] # if day i not need to cover
            else:
                dp[i] = min(dp[max(0,i-1)]+costs[0], dp[max(0,i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
        return dp[days[-1]]

if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets([1,4,6,7,8,20], [2,7,15])) # 11
    print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])) # 17



    