import math

def taylor_series_sin(x, n_terms):
    
    sin_approx = 0
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
        sin_approx += term
    return sin_approx

x = math.radians(30)  
n_terms = 10          
result = taylor_series_sin(x, n_terms)
print(f"sin({math.degrees(x)}°) ≈ {result}")
