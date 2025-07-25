import sympy as sp

x, y, l = sp.symbols('x y l')

f = x**2 + y**2

g = x + y - 1

L = f + l * g

dL_dx = sp.diff(L, x)
dL_dy = sp.diff(L, y)
dL_dl = sp.diff(L, l)

solutions = sp.solve([dL_dx, dL_dy, dL_dl], (x, y, l))

from scipy.optimize import minimize

def objective(vars):
    x, y = vars
    return x**2 + y**2

def constraint(vars):
    x, y = vars
    return x + y - 1 # Constraint: x + y - 1 = 0

x0 = [0, 0]

constraints = ({'type': 'eq', 'fun': constraint})

result = minimize(objective, x0, constraints=constraints)

