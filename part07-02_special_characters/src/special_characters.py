import string


def main() -> None:
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])


def separate_characters(my_string: str) -> tuple[str, str, str]:
    letters = ""
    punctuations = ""
    others = ""
    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuations += char
        else:
            others += char

    return letters, punctuations, others


# main()
