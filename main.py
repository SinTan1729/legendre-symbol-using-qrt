#!/usr/bin/env python3

# Prime checking function
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(3, x - 1):
        if x % i == 0:
            return False
    return True


def main() -> None:
    for i in range(1, 100):
        if is_prime(i):
            print(i)


if __name__ == "__main__":
    main()
