class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                # put related index into 0
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
                print(s[i * i:n:i])
        return sum(s)

    def countPrimes(self, n: int) -> int:
        # count primes in [2, n)        
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0], prime[1] = False, False

        for i in range(2, n):
            if prime[i]:
                # i 的倍数不可能是prime
                for j in range(2*i, n, i):
                    prime[j] = False
        return sum(prime)

    # Sieve of Eratosthenes
    # Time: O(NloglogN)
    def countPrimes(self, n: int) -> int:
        # count primes in [2, n)        
        if n <= 2:
            return 0
        prime = [True] * n
        prime[0], prime[1] = False, False

        # for i in range(2, n):
        # 由于乘法因子对称性，i只需要[2, sqrt(n)]
        for i in range(2, int(sqrt(n))):
            if prime[i]:
                # i 的倍数不可能是prime
                # for j in range(2*i, n, i):
                # j只需要从i*i开始，5*3已经被3*5考虑过了
                for j in range(i*i, n, i):
                    prime[j] = False
        return sum(prime)

s = Solution()
print(s.countPrimes(10))

