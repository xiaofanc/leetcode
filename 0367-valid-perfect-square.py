class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	# find f(x) = 0
    	# Newton's method
        x = num
        while x*x > num:
            x = (x + num/x) // 2
        return x*x == num
            
    def isPerfectSquare(self, num: int) -> bool:
        #n^2 = 1+3+5+..+(2n-1)
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    # binary search: O(logn)
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

if __name__ == '__main__':
	s = Solution()
	print(s.isPerfectSquare(16))
	print(s.isPerfectSquare(14))