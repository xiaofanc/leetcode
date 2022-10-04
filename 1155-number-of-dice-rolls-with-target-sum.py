
class Solution:
    # Time: O(NxTxK), Space: O(NxT)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # [1,2,3...k], [1,2,3...k],...
        # select from 1-k n times that can sum up to target
        memo = {}
        def backtracking(i, combs):
            if (i, combs) in memo:
                return memo[(i, combs)]
            if i == n and combs == 0:
                return 1
            if i >= n:
                return 0
            res = 0   
            for j in range(1, k+1):
                if combs-j < 0:
                    break
                res += backtracking(i+1, combs-j)
            res = res % (10**9+7)
            memo[(i, combs)] = res
            return res
        
        return backtracking(0, target)

    # bottom-up DP
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # memo[i][currSum] = memo[i+1][currSum+j] for j in range[1,k]
        dp = [[0] * (target+1) for j in range(n+1)]
        dp[n][target] = 1
        
        for i in range(n-1, -1,-1):
            for j in range(target+1):
                ways = 0
                
                # iterate over the possible value for current dice
                for v in range(1, min(k, target-j)+1):
                    ways += dp[i+1][j+v] % (10**9+7)
                
                dp[i][j] = ways
        return dp[0][0] % (10**9+7)

    # top-down DP
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # memo[i][currSum] = memo[i-1][currSum-j] for j in range[1,k]
        dp = [[0] * (target+1) for j in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for cursum in range(1, target+1):
                ways = 0
                for j in range(1, min(k, cursum)+1):
                    ways += dp[i-1][cursum-j]
                dp[i][cursum] = ways % (10**9+7)
        
        return dp[n][target] % (10**9+7)

if __name__ == '__main__':
    s = Solution()
    print(s.numRollsToTarget(1,6,3)) # 1
    print(s.numRollsToTarget(2,6,7)) # 6


