import math

class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        def minNumsquares(k):
            #base case
            if k in square_nums:
                return 1
            min_num = float("inf")
            #find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumsquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num
        return minNumsquares(n)
            
    def numSquares(self, n: int) -> int:
        # dp[i] to store the least number of perfect square numbers that sum to i   
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]
        
if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(55))