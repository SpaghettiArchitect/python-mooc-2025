def most_common_character(large_string: str) -> str:
    counter = 0
    most_common = ""
    for char in large_string:
        repetitions = large_string.count(char)
        if repetitions > counter:
            counter = repetitions
            most_common = char
    return most_common


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))  # b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))  # e
