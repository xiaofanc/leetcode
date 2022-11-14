# find the greast common divisor of two nums
def computeGCD0(x, y):
	if x > y:
		small = y 
	else:
		small = x
	for i in range(1, small+1):
		if x % i == 0 and y % i == 0:
			gcd = i
	return gcd

def computeGCD(x, y):
	if x == 0:
		return y
	return computeGCD(y % x, x)

# find the least common multiple of two numbers
# findLCM(4, 6) = 12 = 4*6//2
def findLCM(x, y):
	hcf = computeGCD(x, y)
	lcm = (x*y)//hcf
	return lcm

print(computeGCD(2,3)) # 1
print(computeGCD(3,2)) # 1
print(computeGCD(4,6)) # 2
print(findLCM(4,6))    # 12