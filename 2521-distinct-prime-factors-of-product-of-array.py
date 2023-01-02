"""
number of distinct prime factors for the numbers
"""
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactors(n):
            c = 2
            while n > 1:
                if n % c == 0:
                    primes.add(c)
                    n = n/c
                else:
                    c += 1

        primes = set()
        for num in nums:
            primeFactors(num)
        return len(primes)
            