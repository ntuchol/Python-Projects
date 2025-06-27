def newton_sqrt(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    # Initial guess
    guess = number / 2.0 if number != 0 else 0.0
    
    for _ in range(max_iterations):
        # Newton's formula: x = x - f(x)/f'(x)
        next_guess = 0.5 * (guess + number / guess)
        
        # Check for convergence
        if abs(next_guess - guess) < tolerance:
            return next_guess
        
        guess = next_guess
    
    raise RuntimeError("Failed to converge to a solution within the maximum iterations.")

# Example usage
number = 25
result = newton_sqrt(number)
print(f"The square root of {number} is approximately {result}")

