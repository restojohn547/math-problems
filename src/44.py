import sympy

def solve_linear_equation(a, b):
    # Solve linear equation ax + b = 0 using SymPy
    x = sympy.Symbol('x')
    eqn = a*x + b
    solution = sympy.solve(eqn, x)
    return solution[0]

# Example usage:
a = 2
b = -3
solution = solve_linear_equation(a, b)
print(solution)  # Output should be -1.5
