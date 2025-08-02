def length_of_longest(words: list[str]) -> int:
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)  # 8
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)  # 7
