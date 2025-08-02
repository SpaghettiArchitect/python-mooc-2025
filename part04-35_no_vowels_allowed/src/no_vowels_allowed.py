def no_vowels(string: str) -> str:
    new_string = string
    for vowel in "aeiou":
        new_string = new_string.replace(vowel, "")
    return new_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))  # "ths s n xmpl"
