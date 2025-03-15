 import random

def get_random_math_problem(minimum=1, maximum=99):
    problem = f"{random.randint(minimum, maximum)} x {random.randint(minimum, maximum)} ="
    answer = int(eval(problem))
    return problem, answer