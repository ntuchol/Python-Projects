import math

def taylor_series_sin(x, n_terms):
    """
    Calculate the Taylor series expansion of sin(x).
    
    Parameters:
    x (float): The value of x (in radians).
    n_terms (int): The number of terms in the Taylor series.
    
    Returns:
    float: Approximation of sin(x) using the Taylor series.
    """
    sin_approx = 0
    for n in range(n_terms):
        # Taylor series term: ((-1)^n * x^(2n+1)) / (2n+1)!
        term = ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
        sin_approx += term
    return sin_approx

# Example usage
x = math.radians(30)  # Convert 30 degrees to radians
n_terms = 10          # Number of terms in the series
result = taylor_series_sin(x, n_terms)
print(f"sin({math.degrees(x)}°) ≈ {result}")