def change_case(orig_string: str) -> str:
    new_string = ""
    for char in orig_string:
        if char.islower():
            new_string += char.upper()
        else:
            new_string += char.lower()
    return new_string


def split_in_half(orig_string: str) -> tuple[str, str]:
    half_point = len(orig_string) // 2
    first_half = orig_string[:half_point]
    second_half = orig_string[half_point:]
    return first_half, second_half


def remove_special_characters(orig_string: str) -> str:
    new_string = ""
    for char in orig_string:
        if char.isdigit() or char.isalpha() or char.isspace():
            new_string += char
    return new_string


if __name__ == "__main__":
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
