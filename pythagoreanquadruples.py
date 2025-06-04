def find_pythagorean_quadruples(limit):
    quadruples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  # Start from 'a' to avoid duplicates
            for c in range(b, limit + 1):  # Start from 'b' to maintain order
                d_squared = a**2 + b**2 + c**2
                d = int(d_squared**0.5)
                if d**2 == d_squared and d <= limit:
                    quadruples.append((a, b, c, d))
    return quadruples

# Example usage
limit = 20
result = find_pythagorean_quadruples(limit)
print("Pythagorean quadruples up to", limit, "are:")
for quadruple in result:
    print(quadruple)
