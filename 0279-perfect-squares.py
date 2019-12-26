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
            

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(55))