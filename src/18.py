import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# Example usage
print(is_prime(7))
print(is_prime(15))
