
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