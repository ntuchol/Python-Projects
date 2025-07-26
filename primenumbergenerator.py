def prime_generator(limit):
    
    if limit <= 1:
        return
    
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, limit + 1, i):
                primes[multiple] = False

    for i in range(2, limit + 1):
        if primes[i]:
            yield i

for prime in prime_generator(50):
    print(prime)
