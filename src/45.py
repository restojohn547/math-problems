def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

result = calculate_sum([1, 2, 3, 4, 5])
print(result)
