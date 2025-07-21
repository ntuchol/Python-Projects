import sympy as sp

x, y, l = sp.symbols('x y l')

# Objective function: f(x,y) = x^2 + y^2
f = x**2 + y**2

# Constraint function: g(x,y) = x + y - 1 = 0
g = x + y - 1

# Lagrangian
L = f + l * g

# Partial derivatives
dL_dx = sp.diff(L, x)
dL_dy = sp.diff(L, y)
dL_dl = sp.diff(L, l)

# Solve the system of equations
solutions = sp.solve([dL_dx, dL_dy, dL_dl], (x, y, l))

# Evaluate the objective function at the solution
# For each solution in 'solutions', substitute x and y back into 'f'

from scipy.optimize import minimize

def objective(vars):
    x, y = vars
    return x**2 + y**2

def constraint(vars):
    x, y = vars
    return x + y - 1 # Constraint: x + y - 1 = 0

# Initial guess for x and y
x0 = [0, 0]

# Define the constraint
constraints = ({'type': 'eq', 'fun': constraint})

# Perform the optimization
result = minimize(objective, x0, constraints=constraints)

# The optimal values for x and y are in result.x