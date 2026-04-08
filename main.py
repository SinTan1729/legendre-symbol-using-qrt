#!/usr/bin/env python3


def is_prime(n: int) -> bool:
    """Check if an integer is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    # No need to check beyond sqrt(n):
    # if n = a * b, one factor ≤ sqrt(n)
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def decompose(n: int) -> dict[int, int]:
    """Decompose an integer."""

    def insert(i: int) -> None:
        out[i] = out.get(i, 0) + 1

    out: dict[int, int] = {}
    if n == 0:
        return {0: 1}
    if n == 1:
        # We do this for readability, returning {} is more common here
        return {1: 1}
    if n < 0:
        insert(-1)
        n = -n

    while n % 2 == 0:
        insert(2)
        n //= 2

    d = 3
    while d * d <= n:
        # At this point, n has no prime factors < d
        while n % d == 0:
            insert(d)
            n //= d
        d += 2

    # If remainder is prime
    if n > 1:
        insert(n)

    return out


def legendre(m: int, n: int) -> int:
    """Calculate the Legendre symbol (m/n)"""
    m = m % n
    if m == 0:
        return 0
    if n == 2:
        return 1
    if not is_prime(n):
        raise Exception("q needs to be a prime.")
    if m == 1:
        return 1
    if m == 2:
        res = n % 8
        if res == 1 or res == 7:
            return 1
        else:
            return -1
    factors = decompose(m)
    out = 1
    for p in factors:
        if n < p or p == 2:
            out *= legendre(p, n) ** factors[p]
        else:
            res1 = p % 4
            res2 = n % 4
            if res1 == 1 or res2 == 1:
                mult = 1
            else:
                mult = -1
            out *= (legendre(n, p) * int(mult)) ** factors[p]
    return out


def main() -> None:
    """Main function, mostly for testing."""
    print(legendre(83, 103), 1)
    print(legendre(17, 19), 1)
    print(legendre(-2, 19), 1)
    print(legendre(5, 7), -1)
    print(legendre(18, 3), 0)
    print(legendre(19, 3), 1)
    print(legendre(17, 3), -1)
    print(legendre(19, 13), -1)


if __name__ == "__main__":
    main()
