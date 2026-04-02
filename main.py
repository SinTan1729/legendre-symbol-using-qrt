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


def main() -> None:
    """Main function, mostly for testing."""
    print(decompose(-7 * 7 * 2 * 2 * 2 * 5 * 9))
    print(decompose(2 * 2 * 5 * 9))
    print(decompose(0))
    print(decompose(1))
    print(decompose(-1))
    print(decompose(2))
    print(decompose(7))
    print(list(filter(is_prime, range(100))))


if __name__ == "__main__":
    main()
