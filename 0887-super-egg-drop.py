# 最坏情况下最少扔几次鸡蛋找到x？

class Solution:
	# sol-1: O(kn^2), TLE
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def dp(k, n):
            # base case
            # 如果只有一个鸡蛋，只能线性扫描1-n
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float("inf")
            # 穷举所有可能的选择i，选择最少扔鸡蛋的次数
            for i in range(1, n+1):
                # 如果鸡蛋碎了，搜索区间 1 <= x < i
                # 如果鸡蛋没碎，搜索区间 i <= x <= n，共n-i层楼
                res = min(res, max(dp(k-1, i-1), dp(k, n-i))+1)
            memo[(k, n)] = res
            return res
        
        return dp(k, n)

    # sol-2: O(knlogn)
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}
        def dp(k, n):
            # base case
            # 如果只有一个鸡蛋，只能线性扫描1-n
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float("inf")
            # 穷举所有可能的选择i，选择最少扔鸡蛋的次数
            # for i in range(1, n+1):
            # 二分搜索i for dp(k-1, i-1) = dp(k, n-i)
            l, r = 1, n
            while l <= r:
                mid = l + (r-l)//2
                broken = dp(k-1, mid-1)
                notb = dp(k, n-mid)
                if broken > notb:
                    r = mid-1
                    res = min(res, broken+1)
                else:
                    l = mid+1
                    res = min(res, notb+1)
            memo[(k, n)] = res
            return res
        
        return dp(k, n)

	# sol-3: O(kn)
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(k+1)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for i in range(1, k+1):
                # dp[i][m-1] 楼上的楼层数，鸡蛋没碎
                # dp[i-1][m-1] 楼下的楼层数，鸡蛋碎了
                dp[i][m] = dp[i][m-1] + dp[i-1][m-1] + 1
        return m

