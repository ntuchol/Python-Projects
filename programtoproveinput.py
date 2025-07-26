from sympy import symbols, Eq, simplify

a, b = symbols('a b')

lhs = a**2 - b**2 
rhs = (a - b) * (a + b)  

theorem = Eq(lhs, rhs)

proof = simplify(lhs - rhs)

if proof == 0:
    print(f"The theorem '{theorem}' is proven to be True!")
else:
    print(f"The theorem '{theorem}' is False.")

from z3 import *

A = Bool('A')
B = Bool('B')

theorem = Or(A, Not(A))

solver = Solver()
solver.add(Not(theorem))  

if solver.check() == unsat:
    print("The theorem is proven to be True!")
else:
    print("The theorem is False.")
