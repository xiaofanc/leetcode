from collections import deque

def q(n):	
	queue = deque()
	while n > 0:
		queue.append(n % 3)
		n /= 3

	while queue:
		print(queue.popleft())

def f(n):
	if n <= 0:
		return 0
	if n == 1:
		return 2
	return f(n-1) + f(n-2)

# print(q(100))
print(f(6))