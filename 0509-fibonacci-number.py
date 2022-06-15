# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def memo(func):
    cache = {}
    def new_func(n):
        if n in cache:
            return cache[n]
        else:
            v = func(n)
            cache[n] = v
            return v
    return new_func

@memo    # Time: O(2^n), space: O(n)
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
    if N < 2:
        return N
    f0, f1 = 0, 1
    for i in range(N-1):
        f0, f1 = f1, f0+f1
    return f1

def fib(self, n: int) -> int:
    if n < 2:
        return n
    prev, cur = 0, 1
    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    return cur
        
def main():
    n = 1
    while n >= 1:
        if fibonacci(n) > n**2:
            print(n, fibonacci(n), n**2)
            break
        else:
            n += 1

if __name__ == '__main__':
    main()

#print fibonacci(0)
#>>> 0
#print fibonacci(1)
#>>> 1
#print fibonacci(15)
#>>> 610