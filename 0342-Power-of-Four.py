
class Solution(object):
	# Time: log4(N)
    def isPowerOfFour(self, n):
        if n == 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1
        
    def isPowerOfFour(self, n):
        maxPower = 15
        for i in range(maxPower+1):
            if 4**i == n:
                return True
        return False