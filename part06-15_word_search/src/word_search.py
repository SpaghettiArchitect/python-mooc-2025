def main() -> None:
    found = find_words("*vokes")
    print(found)


def find_words(search_term: str):
    dictionary = load_dictionary("words.txt")
    results = []
    if "." in search_term:
        results = check_word_dots(dictionary, search_term)
    elif "*" in search_term:
        results = check_word_asterisk(dictionary, search_term)
    else:
        if search_term in dictionary:
            results.append(search_term)
    return results


def check_word_dots(dictionary: list[str], search_term: str) -> list[str]:
    results = []
    for word in dictionary:

        if len(word) != len(search_term):
            continue

        is_match = True
        for char in range(len(search_term)):
            if search_term[char] == word[char] or search_term[char] == ".":
                continue
            else:
                is_match = False
                break

        if is_match:
            results.append(word)

    return results


def check_word_asterisk(dictionary: list[str], search_term: str) -> list[str]:
    asterik_position = "start"
    rest_of_word = ""
    if search_term[-1] == "*":
        asterik_position = "end"
        rest_of_word = search_term[:-1]
    else:
        rest_of_word = search_term[1:]

    results = []
    if asterik_position == "start":
        for word in dictionary:
            if word.endswith(rest_of_word):
                results.append(word)
    else:
        for word in dictionary:
            if word.startswith(rest_of_word):
                results.append(word)

    return results


def load_dictionary(filename: str) -> list[str]:
    dictionary = []
    with open(filename) as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


# main()
