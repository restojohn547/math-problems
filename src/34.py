import numpy as np

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Parameters:
    numbers (list): A list of numbers.
    
    Returns:
    float: The average of the input numbers.
    """
    return sum(numbers) / len(numbers)

# Test the function
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"The average is: {average}")
