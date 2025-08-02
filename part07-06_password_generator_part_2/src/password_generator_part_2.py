from string import ascii_lowercase, digits
from random import randint, shuffle, choice


def main() -> None:
    for i in range(10):
        print(generate_strong_password(3, True, True))


def generate_strong_password(n: int, add_numbers: bool, add_special_char: bool) -> str:
    char_pool = list(ascii_lowercase)
    chosen_char = []

    # Ensure at least one char from a-z
    chosen_char.append(choice(char_pool))

    # Ensure at least one digit
    if add_numbers:
        chosen_char.append(choice(list(digits)))
        char_pool += list(digits)

    # Ensure at least one special char
    if add_special_char:
        chosen_char.append(choice(list("!?=+-()#")))
        char_pool += list("!?=+-()#")

    shuffle(char_pool)

    for _ in range(0, n - len(chosen_char)):
        i = randint(0, len(char_pool) - 1)
        chosen_char += char_pool[i]

    shuffle(chosen_char)

    passwd = ""
    for char in chosen_char:
        passwd += char

    return passwd


# main()
