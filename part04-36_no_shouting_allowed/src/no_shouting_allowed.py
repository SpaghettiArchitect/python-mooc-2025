def no_shouting(list_of_strings: list[str]) -> list[str]:
    no_upper_list = []
    for word in list_of_strings:
        if not (word.isupper()):
            no_upper_list.append(word)
    return no_upper_list


if __name__ == "__main__":
    my_list = [
        "ABC",
        "def",
        "UPPER",
        "ANOTHERUPPER",
        "lower",
        "another lower",
        "Capitalized",
    ]
    pruned_list = no_shouting(my_list)
    print(pruned_list)  # ['def', 'lower', 'another lower', 'Capitalized']
