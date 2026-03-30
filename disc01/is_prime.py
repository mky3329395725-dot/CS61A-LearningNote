def is_prime(n):
    """
    Returns True if a positive integer n is a prime number and False otherwise.

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 2
    while (i < n):
        if (n % i == 0):
            return True
        i += 1
    return False