def find_prime_factors(n):
    """
    Calculate prime factors of a given number n.
    
    Parameters:
    n (int): The number to calculate prime factors for.
    
    Returns:
    list: A list containing all prime factors of n.
    """
    if n % 2 == 0:
        return [2]
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            return [factor] + find_prime_factors(n // factor)
        factor += 2
    return [n]

# Example usage
print(find_prime_factors(56))  # Output: [2, 2, 7]
