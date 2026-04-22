#!/usr/bin/env python3

from sage.arith.misc import legendre_symbol
import json


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
    m = m % n
    # Takes care of the zero case
    if m == 0:
        return 0
    if n == 2 or not is_prime(n):
        raise Exception("q needs to be an odd prime.")
    # Speciel case for 1
    if m == 1:
        return 1
    # Speciel case for even prime
    if m == 2:
        res = n % 8
        if res == 1 or res == 7:
            return 1
        else:
            return -1
    factors = decompose(m)
    out = 1
    # Code that follows uses the quadratic reciprocity theorem
    for p in factors:
        # No need to check if zero here, dealt with above
        if n < p or p == 2:
            out *= legendre(p, n) ** factors[p]
        else:
            # If the conditions above are both false, then we can use QRT to flip the legendre symbol
            res1 = p % 4
            res2 = n % 4
            if res1 == 1 or res2 == 1:
                mult = 1
            else:
                mult = -1
            out *= (legendre(n, p) * int(mult)) ** factors[p]
    return out


def quadratic_residue_primes(n: int, p: int) -> int:
    """Check if some integer is a quadratic residue modulo a prime"""
    if p <= 2 or (not is_prime(p)):
        raise Exception("Modulus must be a prime larger than two")
    n = n % p
    return n == 0 or legendre_symbol(n, p) == 1


def quadratic_residue(a: int, n: int) -> int:
    """Check if some integer is a quadratic residue modulo another integer"""
    if n <= 1:
        raise Exception(" n must be larger than 1")
    a = a % n
    if a == 0:
        return True
    dec = decompose(n)
    for p in dec:
        if p > 2 and (not quadratic_residue_primes(a, p)):
            return False
        if p == 2:
            r = dec[p]
            if r >= 3 and not (a % 8 == 1):
                return False
            if r >= 2 and not (a % 4 == 1):
                return False
    return True


def main() -> None:
    """Main function, used for testing."""
    with open("data.txt", "r") as f:
        for line in f.readlines():
            if line.startswith("#"):
                continue
            m, n, o = json.loads(line)
            lg = legendre(m, n)
            if lg != o:
                raise Exception(f"(({m},{n}) = {lg}, but should be {lg}!)")

    prime_checks = [
        [7, True],
        [31, True],
        [111, False],
        [7919, True],
        [10791, False],
    ]
    for p, b in prime_checks:
        if is_prime(p) != b:
            raise Exception(f"is_prime({p}) should not be {not b}!")

    decompose_checks = [
        [7, {7: 1}],
        [8, {2: 3}],
        [1, {1: 1}],
        [-1, {-1: 1}],
        [-18, {-1: 1, 2: 1, 3: 2}],
        [60, {2: 2, 3: 1, 5: 1}],
    ]
    for n, d in decompose_checks:
        assert isinstance(n, int)
        dn = decompose(n)
        if dn != d:
            raise Exception(f"decompose({n}) = {d}, but found {dn}!")

    residue_tests = [
        [17, 32, True],
        [3, 16, False],
        [73, 144, True],
        [21, 144, False],
        [5, 7, False],
    ]
    for a, n, b in residue_tests:
        if quadratic_residue(a, n) != b:
            raise Exception(f"Quadratic residue ({a},{n}) must be {b}.")

    print("All tests passed!")


if __name__ == "__main__":
    main()
