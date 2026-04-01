#!/usr/bin/env python3

# Prime checking function
def is_prime(n: int) -> bool:
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
    if n < 0:
        raise ValueError

    def aux(i: int) -> dict[int, int]:
        di = decompose(int(n / i))
        j = di.get(i, 0) + 1
        di[i] = j
        return di

    if n % 2 == 0:
        return aux(2)
    for i in [2] + list(range(3, int(pow(n, 0.5)) + 1, 2)):
        if n % i == 0:
            return aux(i)
    return {n: 1}


def main() -> None:
    print(decompose(7 * 7 * 2 * 2 * 2 * 5 * 9))


if __name__ == "__main__":
    main()
