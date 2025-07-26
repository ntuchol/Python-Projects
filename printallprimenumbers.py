def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

start_range = 1
end_range = 50
print(f"Prime numbers between {start_range} and {end_range}:")
print_primes_in_range(start_range, end_range)
