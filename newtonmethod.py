def newton_sqrt(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    guess = number / 2.0 if number != 0 else 0.0
    
    for _ in range(max_iterations):
        next_guess = 0.5 * (guess + number / guess)
        
        if abs(next_guess - guess) < tolerance:
            return next_guess
        
        guess = next_guess
    
    raise RuntimeError("Failed to converge to a solution within the maximum iterations.")

number = 25
result = newton_sqrt(number)
print(f"The square root of {number} is approximately {result}")
