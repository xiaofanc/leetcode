"""
Given tiles of dimensions 1x1x2, determine how many ways they can be arranged to form a rectangular solid of dimensions 2x2xn.
if n = 1, there are two ways of doing so:
	Lay the tiles north and south or east and west.
The function should return an array of integers that represent the number of ways each solid can be formed.
The number of permutations increases quickly, so the return value should be modulo (10^9+7).
"""

class Solution: # Time: O(n)
	# pass all
	def dominos0(self, n):
	    if n == 1:
	        return 2
	    
	    MOD = int(1e9 + 7)
	    # full
	    # f(n) = 2 * f(n - 1) + 5 * f(n - 2) + 4 * p(n - 1)
	    # 2: vertical + horizontal
	    # 5: all vertical + 4 * (2 ver, 2 hor)
	    # 4: (1 hor), 4 orientations
	    # cannot use 4 * p(n) because there are overlaps between f(n - 2)
	    f = [1, 2]
	    
	    # partial, one orientation, top layer is vertical
	    # p(n) = f(n - 2) + p(n - 1)
	    p = 0  # p(1)
	    
	    for _ in range(n - 1):
	        f, p = [f[1], (5 * f[0] + 2 * f[1] + 4 * p) % MOD], (p + f[0]) % MOD
	        # print(f[1])
	    return f[1]	

	# pass all
	def dominos1(self, n):
		mod = int(1e9 + 7)
		dp1 = [1] * (n+2)
		dp2 = [0] * (n+1)
		dp1[1] = 2 
		dp2[1] = 4
		for i in range(2, n+1):
			dp2[i] = dp2[i-1] + 4 * dp1[i-1] % mod
			dp1[i] = (dp2[i-1] + 2 * dp1[i-1] + dp1[i-2]) % mod
		return dp1[n]

	def dominos2(self, n):    
	    MOD = int(1e9 + 7)
	    def f(n):
	        if n == 0:
	            return 1
	        if n == 1:
	            return 2 
	        return (2 * f(n-1) + 5 * f(n-2) + 4 * g(n-1)) % MOD
	    # partial, one orientation, top layer is vertical
	    def g(n):
	        # n >= 2
	        if n == 1:
	            return 0

	        return (g(n-1) + f(n-2)) % MOD    
	    
	    return f(n)

	def dominos3(self,n):
		def f(n):
			if n == 0:
				return 1
			if n == 1:
				return 2 
			return 2*g(n) + 2*g(n-1) + f(n-2)

		def g(n):
			if n == 0:
				return 0 
			if n == 1:
				return 1 

			return g(n-1) + f(n-1)
		return f(n) % (10**9+7)

if __name__ == '__main__':
	s = Solution()
	print(s.dominos1(1)) #2
	print(s.dominos1(2)) #9
	print(s.dominos1(3)) #32
	print(s.dominos1(100)) #828630254


