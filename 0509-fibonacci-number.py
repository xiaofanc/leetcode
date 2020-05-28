# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current+after
    return current 

def fib(self, N):
    """
    :type N: int
    :rtype: int
    """
    if N == 0:
        return 0
    if N == 1:
        return 1
    f0, f1 = 0, 1
    for i in range(N-1):
        f0, f1 = f1, f0+f1
    return f1

#print fibonacci(0)
#>>> 0
#print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610