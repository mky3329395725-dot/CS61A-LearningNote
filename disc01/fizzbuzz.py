def fizzbuzz(n):
    """Print all numbers lower than n and greater than 0,
    but print 'fizz' when the number is divisible by 3,
    print 'buzz' when it is divisible by 5,
    print 'fizzbuzz' when it is divisible by both 3 and 5
    >>>result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None"""
    i = 1
    while(i <= n):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)
        i += 1
    return None