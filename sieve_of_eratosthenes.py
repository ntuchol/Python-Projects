def sieve_of_eratosthenes(n):
primes = [True] * (n + 1)
primes[0] = primes[1] = False
p = 2
while p * p <= n:
if primes[p]:
for i in range(p * p, n + 1, p):
primes[i] = False
p += 1
return [i for i, prime in enumerate(primes) if prime]

# Driver code
if __name__ == "__main__":
num = 30
print(f"Prime numbers up to {num}: {sieve_of_eratosthenes(num)}")