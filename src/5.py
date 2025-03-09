
import random

def get_random_math_problem():
    operands = [1, 2, 3, 4, 5]
    operation = ["+", "-", "*", "/"]
    problem = f"{operands[0]} {operation[random.randint(0, len(operation)-1)]} {operands[1]} = "
    return problem