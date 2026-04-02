#!/usr/bin/env python3

from math import isqrt


def is_prime(n: int) -> bool:
    """Check if an integer is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True


def decompose(n: int) -> dict[int, int]:
    """Decompose an integer."""

    def aux(n: int, start: int, carry: dict[int, int]) -> dict[int, int]:
        def insert(dict: dict[int, int], i: int) -> dict[int, int]:
            j = dict.get(i, 0) + 1
            dict[i] = j
            return dict

        if n < 0:
            return aux(-n, 2, {-1: 1})

        if n == 0:
            return {0: 1}

        if n == 1:
            if carry:
                return carry
            else:
                return {1: 1}

        if start == 2 and n % 2 == 0:
            return aux(n // 2, 2, insert(carry, 2))
        if start == 2:
            start = 3
        for i in range(start, isqrt(n) + 1, 2):
            if n % i == 0:
                return aux(n // i, i, insert(carry, i))
        return insert(carry, n)

    return aux(n, 2, {})


def main() -> None:
    """Main function, mostly for testing."""
    print(decompose(-7 * 7 * 2 * 2 * 2 * 5 * 9))
    print(decompose(2 * 2 * 5 * 9))
    print(decompose(0))
    print(decompose(1))
    print(decompose(-1))
    print(decompose(2))
    print(decompose(7))


if __name__ == "__main__":
    main()
