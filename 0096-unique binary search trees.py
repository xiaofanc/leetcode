"""
DP[0] = 1
DP[1] = DP[0] * DP[0]
DP[2] = DP[0] * DP[1] + DP[1] * DP[0]
DP[3] = DP[0] * DP[2] + DP[1] * DP[1] + DP[2] * DP[0]
....

"""
class Solution:
    def numTrees(self, n: int) -> int:
        DP = [0]*(n+1)
        # base case: 
        DP[0], DP[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                DP[i] += DP[j]*DP[i-1-j]
        return DP[-1]
                
if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3) == 5)