"""
sqrt(x) <= x//2 for x >= 4
"""
from math import e, log
class Solution:
    def mySqrt0(self, x: int) -> int:
        if x < 2:
            return x
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right*right > x else right
        
    #binary search: O(logn)
    def mySqrt1(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if mid*mid > x:
                right = mid - 1
            elif mid*mid < x:
                left = mid + 1
            else:
                return mid
            print(left, right, mid)
        return right # right is the first number less than sqrt(x)

    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        l, r = 1, x
        while l <= r:
            mid = l + (r-l)//2
            print(l, mid, r)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        # outside the loop l > r
        # we are rounding down the result, so r is returned
        return r
        
    #newton's method
    def mySqrt2(self, x: int) -> int:
        if x < 2:
            return x
        x0 = x
        x1 = (x0 + x/x0) / 2
        while abs(x0 - x1) >= 1
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)

s = Solution()
print(s.mySqrt0(8))
