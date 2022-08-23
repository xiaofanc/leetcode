class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost + [0]
        dp = [0] * (len(cost))
        for i in range(1, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        print("dp", dp)
        return dp[-1]
        
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1] + cost[i], cost[i-2] + cost[i])
        return min(cost[-1], cost[-2])

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 0 or n == 1:
            return 0
        f1, f2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f1, f2 = f2, min(f1, f2) + cost[i]
        return min(f1, f2)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        cost = cost + [0]  # why add 0? the cost of top floor
        f1, f2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f1, f2 = f2, min(f1, f2) + cost[i]
        return f2

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]) == 15)
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6)
    