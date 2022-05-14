


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost + [0]
        dp = [0] * (len(cost))
        for i in range(1, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        print("dp", dp)
        return dp[-1]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

if __name__ == '__main__':
	s = Solution()
	print(s.minCostClimbingStairs([10,15,20])) #15