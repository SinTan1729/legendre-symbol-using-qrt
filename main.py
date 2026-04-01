# /usr/bin/env python3


# Modulus function
def mod(x, n):
    if not isinstance(n, int) or not isinstance(x, int):
        raise ValueError("Must be an integer")
    if n == 0:
        raise ValueError("n cannot be zero")
    value = x % n
    return value


# Prime function
def is_prime(x):
    if not isinstance(x, int):
        raise ValueError("Must be an integer")
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(3, x - 1):
        if x % i == 0:
            return False
    return True
