
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        m = len(nums)
        res = 0
        def isPrime(n):
            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            # 1 is not a prime number
            return n >= 2 
            
        for i in range(m):
            if isPrime(nums[i][i]):
                res = max(res, nums[i][i])
            if isPrime(nums[i][m-i-1]):
                res = max(res, nums[i][m-i-1])
        return res

