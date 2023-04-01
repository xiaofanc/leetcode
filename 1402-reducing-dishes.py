"""
Cook the current dish and add the value satisfaction[index] * time; the next dish will be cooked at time time + 1, so add the value of dp[index + 1]time + 1].
Skip the current dish, and then the next dish will be cooked at time time, hence the value dp[index + 1][time]
"""
class Solution:
	# TOP-DOWN
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}
        def dp(i, time):
            if i == len(satisfaction):
                return 0
            if (i, time) in memo:
                return memo[(i, time)]
            res = max(satisfaction[i]*time + dp(i+1, time+1), dp(i+1, time))
            memo[(i, time)] = res
            return res
        return dp(0, 1)


    # BOTTOM-UP
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        # dp[i][t]: max sum starting from dish i
        dp = [[0 for i in range(n+2)] for i in range(n+1)]
        for i in range(n-1, -1, -1):
            for time in range(n, 0, -1):
                # print(i, time)
                dp[i][time] = max(satisfaction[i] * time + dp[i+1][time+1], dp[i+1][time])
        
        return dp[0][1]


    # BOTTOM-UP
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        prev = [0 for i in range(n+2)]
        for i in range(n-1, -1, -1):
            # dp[t]: max sum starting from time t
            dp = [0 for i in range(n+2)]
            for time in range(n, 0, -1):
                # print(i, time)
                dp[time] = max(satisfaction[i] * time + prev[time+1], prev[time])
            prev = dp
        
        return prev[1]



        