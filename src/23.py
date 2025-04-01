import numpy as np
from scipy.special import comb

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient(n, k):
    return comb(n, k) // (comb(k, 0) * comb(n - k, 1))

print(binomial_coefficient(5, 2))
