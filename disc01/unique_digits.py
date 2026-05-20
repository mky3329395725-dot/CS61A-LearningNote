def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    if n == 0:
        return 1.
    for i in range(10):
        if has_digit(n,i):
            sum += 1
    return sum





def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    if n == 0:
        return k == 0
    while(n != 0):
        last = n % 10
        if last == k:
            return True
        n //= 10
    return False
