import random

def solve_math_problem(problem):
    # Define a dictionary to map each problem type to a function that solves it
    problem_types = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y
    }
    
    # Get the problem type and operands from the problem string
    problem_type, operand1, operand2 = problem.split()
    
    # Use the dictionary to call the appropriate function to solve the problem
    solution = problem_types[problem_type](int(operand1), int(operand2))
    
    return solution

# Test the function with a random math problem
problem = 'add 3 5'
solution = solve_math_problem(problem)
print(f"The solution is {solution}")