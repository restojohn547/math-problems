import random

def generate_math_problem(difficulty):
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operation (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])

    # Evaluate the problem and return the answer
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2

# Call the function with a difficulty level of 3
print(generate_math_problem(3))
