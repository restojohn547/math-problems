def square_root(num):
    if num > 0:
        return num ** 0.5
    else:
        raise ValueError("Input must be positive")

try:
    print(square_root(-1))
except ValueError as e:
    print(e)
