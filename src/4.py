from random import randint

def get_random_math_problem(difficulty=2):
    # Generate two random numbers between 1 and 10
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    
    # Choose a random operation (+, -, *, /)
    ops = ["+", "-", "*", "/"]
    op = ops[randint(0, len(ops) - 1)]
    
    # Generate the problem
    if op == "+":
        return f"{num1} {op} {num2} = ?"
    elif op == "-":
        return f"{num1} {op} {num2} = ?"
    elif op == "*":
        return f"{num1} {op} {num2} = ?"
    else:
        return f"{num1} {op} {num2} = ?"
