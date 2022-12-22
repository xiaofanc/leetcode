"""
给幂运算求模
- 如何处理用数组表示的指数？
不能转化成一个数，太大会溢出
B = [1, 5, 6, 4]
a[1,5,6,4] =a4*a[1,5,6,0] = a4*(a[1,5,6])10 -> recursion
superPow(a, [1,5,6,4]) => superPow(a, [1,5,6])
Part1 = mypow(a, last), Part2 = mypow(superPow(a, b), 10)
Return Part1 * Part2

- 如何处理mod运算？
(a*b % k) = (a % k)(b % k) % k
先对a求模，再对乘法结果求模，保证res *= a时两个因子小于base
"""
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337

        def mypow(a, p):
            # calculate a^p % base
            # (a*b % base) = (a % base)(b % base) % base
            res = 1
            # 先对a求模
            a %= base
            for i in range(p):
                res *= a
                res %= base
            return res
        
        if len(b) == 0:
            return 1
        last = b.pop()
        p1 = mypow(a, last)
        p2 = mypow(self.superPow(a, b), 10)
        # 每次乘法都要求模
        return (p1 * p2) % base

		
		# a^b = a x a^(b-1), b is odd = a^(b/2)^2, b is even
        def mypow(a, k):
            # calculate a^k % base
            # (a*b % k) = (a % k)(b % k) % k
            if k == 0:
                return 1
            a %= base
            if k % 2 == 1:
                return (a * mypow(a, k-1)) % base
            else:
                sub = mypow(a, k/2)
                return (sub * sub) % base



                



