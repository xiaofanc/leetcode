class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
        
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n      # 二进制运算
        # return n & (n-1) == 0   # 二进制运算

if __name__ == '__main__':
	s = Solution()
	print(s.isPowerOfTwo(16))
	print(s.isPowerOfTwo(218))

