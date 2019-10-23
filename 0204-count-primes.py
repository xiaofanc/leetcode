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

s = Solution()
print(s.countPrimes(10))