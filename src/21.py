import random

def create_random_string(length):
    """
    Generates a random string of specified length.
    
    Args:
        length (int): The length of the random string.
    
    Returns:
        str: A randomly generated string of the given length.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def main():
    print(create_random_string(10))  # Generate a random 10-character string
    print(create_random_string(20))  # Generate a random 20-character string

if __name__ == "__main__":
    main()
