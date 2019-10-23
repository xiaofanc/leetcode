d = {i: i * 100 for i in range(1,11)}
print(d.values())

d = {i: chr(i) for i in range(ord('a'), ord('z')+1)}
print(d) 

d = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(d) 

d = {x: x**2 for x in range(-5,6)}
print(d) 

d = {x: [x]*x for x in range(1,6)}
print(d) 

d = set(x**2 for x in range (-5,6))
d = {x**2 for x in range (-5,6)}
print(d) 

d = {i: [[x] for x in range(i+1)] for i in range(4)}
print(d) 

def fib(n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

d = fib(4)
print(d)
s = {x:{i: fib(i) for i in range(x+1)} for x in range(5)}
print(s)

a = "Let's take LeetCode contest"
a = a.split(' ',1)
print(a)
