def find_factors(number):
    if number == 0:
        return "Factors of 0 are undefined."
    
    factors = []
    for i in range(1, abs(number) + 1):
        if number % i == 0:
            factors.append(i)
            if i != abs(number) // i:  # Avoid duplicates for perfect squares
                factors.append(-i)
    
    # Remove 0.0 factors and convert negatives to absolute values
    factors = [abs(factor) for factor in factors if factor != 0.0]
    return sorted(set(factors))

# Example usage
num = -12
print(f"Factors of {num}: {find_factors(num)}")