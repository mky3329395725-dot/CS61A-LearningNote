def fizzbuzz(n):
    i = 1
    while(i <= n):
        if (n % i == 3 and n % i == 5):
            print("fizzbuzz")
        elif (n % i == 3):
            print("fizz")
        elif (n % i == 5):
            print("buzz")
        else:
            print(i)
    return None