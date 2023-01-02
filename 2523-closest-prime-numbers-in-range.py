"""
Find two cloest prime numbers between left and right
Difference between two consecutive primes is called Prime Gap. 
There is only one gap of 1 (3 - 2).
There are many primes with the gap of 2 - they are called twin primes.
So, we exit early if we find a gap < 3, which improves runtime to 0 ms.
"""

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def findPrimes(left, n):
            primes = [True]*n
            primes[0] = primes[1] = False
            for i in range(2, int(math.sqrt(n))+1):
                if primes[i]:
                    for j in range(i*i, n, i):
                        primes[j] = False
            return [i for i in range(left, n) if primes[i]]
        
        res = [-1,-1]
        primes = findPrimes(left, right+1)
        if len(primes) == 1:
            return res
        d = float('inf')
        for i in range(len(primes)-1):
            if primes[i+1] - primes[i] < d:
                res = [primes[i], primes[i+1]]
                d = primes[i+1] - primes[i]
                if d <= 2:
                    return res
        return res
