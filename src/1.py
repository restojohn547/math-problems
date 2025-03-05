 import random
 
def get_random_math_problem():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*', '/'])
    problem = f'{num1} {operator} {num2}'
    return eval(problem)