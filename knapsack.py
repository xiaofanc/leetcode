"""
一个可装载重量为w的背包和n个物品，每个物品有重量和价值两个属性。其中第i个重量为wt[i]，价值为val[i]。
最多能装的价值是多少？
状态：背包重量，可选择的物品
选择：装进背包，不装进背包

dp[i][j]: 对于前i个物品，当前背包的容量为j时可以装的最大价值。

for i in range(N):
	for j in range(W):
		dp[i][j] = max(
		dp[i-1][j]                 # i不装进背包
		dp[i-1][j-wt[i]]+val[i]    # i装进背包
		)
"""

def knapsack(W, N, wt, val):
	dp = [[0 for j in range(W+1)] for i in range(N+1)]
	for i in range(1, N+1):
		for j in range(1, W+1):
			if j < wt[i]: # 背包容量不够了
				dp[i][j] = dp[i-1][j]
			else:  # 装或不装的最大价值
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i]]+val[i])
	return dp[N][W]
