import random

def get_random_code():
    return ''.join(random.choices('1234567890abcdef', k=10))
