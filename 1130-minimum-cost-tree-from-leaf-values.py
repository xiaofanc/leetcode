from functools import lru_cache
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # for each node
        # return sum as sum of root and subtree 
        # return max as and max of subtree 
        #recursion
        def sum_max(arr):
            n = len(arr)
            if n == 1:
                return arr[0], arr[0]
            if n == 2:
                prod = arr[0]*arr[1]
                return sum(arr)+prod, max(arr)
            else:
                minsum, minmax = float("inf"), float("inf")
                for i in range(1, n):
                    head, tail = arr[:i], arr[i:]
                    sumh, maxh = sum_max(head)
                    sumt, maxt = sum_max(tail)
                    minsum = min(minsum, maxh*maxt + sumh + sumt)
                    minmax = min(minmax, max(maxh, maxt))
                return minsum, minmax
        s, m = sum_max(arr)
        return s - sum(arr)

    #memorization
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}
        def dp(i, j):
            if j<= i:
                return 0
            if (i,j) not in self.memo:
                res = float("inf")
                for k in range(i+1, j+1):
                    res = min(dp(i, k-1) + dp(k, j) + max(arr[i:k])*max(arr[k:j+1]), res)
                self.memo[(i,j)] = res
            return self.memo[(i,j)]
        return dp(0, len(arr)-1)

    #memorization
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j<= i:
                return 0
            return min(dp(i,k-1) + dp(k, j) + max(arr[i:k])*max(arr[k:j+1]) for k in range(i+1, j+1))
        return dp(0, len(arr)-1)

    # upper diagonal traversal
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        for w in range(1,n):
            for i in range(n-w):
                j = i+w
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + max(arr[i:k+1])*max(arr[k+1:j+1]) for k in range(i,j))
        return dp[0][-1]



if __name__ == '__main__':
    s = Solution()
    print(s.mctFromLeafValues([6,2,4]) == 32)