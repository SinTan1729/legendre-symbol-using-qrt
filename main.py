#!/usr/bin/env python3

# Prime checking function
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(pow(x, 0.5)) + 1, 2):
        if x % i == 0:
            return False
    return True


def main() -> None:
    count = 0
    for i in range(1, 100):
        if is_prime(i):
            print(i)
            count += 1
    print("Count:", count)


if __name__ == "__main__":
    main()
