import random

def get_random_math_problem(n):
    numbers = list(range(1, n+1))
    problem_type = random.choice(['addition', 'subtraction', 'multiplication', 'division'])
    if problem_type == 'addition':
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        return f'{num1} + {num2}'
    elif problem_type == 'subtraction':
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        return f'{num1} - {num2}'
    elif problem_type == 'multiplication':
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        return f'{num1} x {num2}'
    else:
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        return f'{num1} / {num2}'