import random
def get_random_number(n):
    if n > 1000 or n < 0:
        raise ValueError("n must be between 0 and 1000")
    return random.randint(0, n)