
def primeFactors(n):
    primes = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            primes.append(c)
            n = n / c
        else:
            c = c + 1
    return primes


def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False 
    return True
    