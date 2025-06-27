import concurrent.futures
import math

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    return math.factorial(n)

def calculate_factorial_future(number):
    """Submits the factorial calculation to a thread pool and returns a future."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(factorial, number)
        return future

if __name__ == '__main__':
    number = 5
    future = calculate_factorial_future(number)
    try:
        result = future.result()
        print(f"The factorial of {number} is {result}")
    except ValueError as e:
        print(f"Error: {e}")