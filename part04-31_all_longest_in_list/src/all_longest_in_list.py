def length_of_longest(words: list[str]) -> int:
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


def all_the_longest(words: list[str]) -> list[str]:
    longest_size = length_of_longest(words)
    longest_words = []
    for word in words:
        if len(word) == longest_size:
            longest_words.append(word)
    return longest_words


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)  # ['eleventh']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
