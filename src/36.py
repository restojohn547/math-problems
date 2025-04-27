def calculate_square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    sqrt = math.sqrt(num)
    return round(sqrt, 2)

try:
    result = calculate_square_root(16)
except ValueError as e:
    print(e)
