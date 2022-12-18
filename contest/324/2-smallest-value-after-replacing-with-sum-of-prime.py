class Solution:
    def smallestValue(self, n: int) -> int:
        
        def primeFactors(n):
            primes = 0
            c = 2
            while(n > 1):

                if(n % c == 0):
                    primes += c
                    n = n / c
                else:
                    c = c + 1
            return primes
        
        done = False
        while not done:
            newn = primeFactors(n)
            if newn == n:
                done = True
            else:
                n = newn
        return newn
            
            
