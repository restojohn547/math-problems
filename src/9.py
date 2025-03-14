from random import randint

def get_random_math_problem(numbers=None):
    if numbers is None:
        numbers = []
    while True:
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        if num1 != num2 and num1 not in numbers and num2 not in numbers:
            break
    return f"{num1} x {num2} = ?"
