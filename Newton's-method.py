# find the cubic root of a number using Newton's method

def cubic_root(num): 
	x = num
	for i in range(num):
		x = 2*x/3 + num/(3*x*x)
	return x

if __name__ == '__main__':
	print(cubic_root(27))
	print(cubic_root(1))
	print(cubic_root(8))
	print(cubic_root(64))