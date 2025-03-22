# Math Problmes - Problem 1: Summation

def summation(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(summation(5))
