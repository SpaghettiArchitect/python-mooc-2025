from string import ascii_lowercase
from random import randint


def main() -> None:
    for i in range(10):
        print(generate_password(8))


def generate_password(n: int) -> str:
    passwd = ""
    for _ in range(n):
        i = randint(0, len(ascii_lowercase) - 1)
        passwd += ascii_lowercase[i]
    return passwd


# main()
