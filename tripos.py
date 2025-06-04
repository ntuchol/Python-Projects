def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)
            if c**2 == c_squared and c <= limit:
                triples.append((a, b, c))
    return triples

limit = 20
pythagorean_triples = find_pythagorean_triples(limit)
print(pythagorean_triples)