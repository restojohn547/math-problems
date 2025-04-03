import numpy as np
from sympy import symbols, solve

x = symbols('x')
equation = 2*x**3 - 5*x**2 + x
roots = solve(equation, x)
print(roots)
