

def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return (n // (10 ** k)) % 10


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return a + b + c - max(a,b,c) - min(a,b,c)


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    i = 0
    while i < k:
        result *= n
        n -= 1
        i += 1
    return result



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(n//k): #运行的次数=i+1，如果从没运行过则i=0
        num = (i+1) * k
        if num <= n:
            print(num)
            count += 1
        else:
            break
    return count

"""也可以倒着来
def divisible_by_k(n,k):
    count = 0
    for i in range(k, n + 1, k):
        print(K)
        count += 1
    return count
"""



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    result = 0
    if y < 0:
        raise ValueError("Input must be nonnegative")
    while y > 0:
        result += y % 10
        y //= 10
    return result

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = 0
    while n: # n == 0时表示假，也就是只要n不是0，那就一直进行
        result = n % 10 # 从个位数开始遍历，看当前位数的数字

        if result == 8: # 如果是8，则开始判断上一个是不是8
            if flag == 1: # 如果上一个也是8，直接返回True
                return True
            flag = 1 # 如果上一个不是8，则进入“第一个8待定”，标注flag = 1
        else:
            flag = 0 # 如果这次不是8，那么清除可能存在的“第一个8待定”

        n //= 10 # 本次验8完毕，除去最后一位
    return False # 如果遍历结束了都没有触发“当前位数是8 -> 上一位已被标注flag = 1也是8”，那么可以确认没有相邻8，返回False

"""
if条件语句可以使用and
def double_eights(n):
    while n: 
        if n % 10 ==8 and n // 10 % 10 == 8:
            return True
        n //= 10
    return False
"""
