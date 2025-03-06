import random

def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Get a random math operator (+, -, *, /)
    op = random.choice(['+', '-', '*', '/'])

    # Create the math problem as a string
    problem = f"{num1} {op} {num2}"

    # Return the problem and the correct answer
    return problem, eval(problem)
