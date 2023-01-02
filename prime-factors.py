
def primeFactors(n):
    primes = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            primes.append(c)
            n = n / c
        else:
            c = c + 1
    return primes

def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False 
    return True
    
# 204. Count Primes
# Sieve of Eratosthenes - find primes in [2, n)
# Time: O(NloglogN)
def findPrimes(self, n: int) -> int:
    # find primes in [2, n)        
    if n <= 2:
        return 0
    prime = [True] * n
    prime[0], prime[1] = False, False

    # for i in range(2, n):
    # 由于乘法因子对称性，i只需要[2, sqrt(n)]
    for i in range(2, int(sqrt(n))+1):
        if prime[i]:
            # i 的倍数不可能是prime
            # for j in range(2*i, n, i):
            # j只需要从i*i开始，5*3已经被3*5考虑过了
            for j in range(i*i, n, i):
                prime[j] = False
    # return sum(prime)
    # return all the primes
    return [i for i in range(2, n) if prime[i]]

# 2523. Closest Prime Numbers in Range
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


