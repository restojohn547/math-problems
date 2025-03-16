def get_random_math_problem(max_value=10):
    # Generate two random integers between 1 and max_value
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    
    # Get a random math operator (+, -, *, /)
    op = ['+', '-', '*', '/'][random.randint(0, 3)]
    
    # Evaluate the problem and return the answer
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2
