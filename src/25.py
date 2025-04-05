import random
from sympy import *
x = symbols('x')
eq1 = Eq(x**2 - 4, 0)
solution1 = solve(eq1, x)

random_solution1 = random.choice(solution1)
print(random_solution1)
