"""
return True if the square root of an integer is an integer, else False
perfectNumber(49) -> True
perfectNumber(50) -> False

"""

def perfectNumber(n):
	if n < 0:
		return False
	if n == 1:
		return True

	def helper(l, r):
		while l <= r:
			m = l + (r-l) // 2
			if m ** 2 == n:
				return True
			elif m ** 2 > n:
				r = m - 1
			else:
				l = m + 1
		return False
	return helper(0, n//2)

print(perfectNumber(0))
print(perfectNumber(1))
print(perfectNumber(49))
print(perfectNumber(50))