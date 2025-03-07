import random

def get_random_math_problem():
    operands = [10, 20, 30]
    operators = ["+", "-", "*"]
    problem = "{} {} {}".format(operands[random.randint(0, 2)], random.choice(operators), operands[random.randint(0, 2)])
    return problem
