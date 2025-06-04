Creating a program to prove theorems is a complex task that typically involves symbolic computation and logic reasoning. Python libraries like SymPy (for symbolic mathematics) and Z3 (a theorem prover) can help. Below is an example of a simple theorem prover using SymPy to verify basic mathematical identities.

Example: Proving a Simple Theorem (e.g., $$a^2 - b^2 = (a - b)(a + b)$$)
Copy the code
from sympy import symbols, Eq, simplify

# Define symbols
a, b = symbols('a b')

# Define the theorem to prove
lhs = a**2 - b**2  # Left-hand side
rhs = (a - b) * (a + b)  # Right-hand side

# Check if the two sides are equivalent
theorem = Eq(lhs, rhs)

# Simplify the difference between LHS and RHS
proof = simplify(lhs - rhs)

# Output the result
if proof == 0:
    print(f"The theorem '{theorem}' is proven to be True!")
else:
    print(f"The theorem '{theorem}' is False.")

Output:

If the theorem is correct, the program will confirm it as true.

Example: Using Z3 for Logical Theorem Proving

For logical theorems, you can use the Z3 library:

Copy the code
from z3 import *

# Define logical variables
A = Bool('A')
B = Bool('B')

# Define a theorem: A OR NOT A is always True (Law of Excluded Middle)
theorem = Or(A, Not(A))

# Create a solver
solver = Solver()
solver.add(Not(theorem))  # Negate the theorem to check for contradictions

# Check if the theorem is valid
if solver.check() == unsat:
    print("The theorem is proven to be True!")
else:
    print("The theorem is False.")

Output:

This will confirm the logical theorem as true if it holds universally.

These examples are basic and can be extended to more complex theorems depending on your needs. For advanced theorem proving, consider integrating Python with specialized tools like Coq, Lean, or Isabelle.