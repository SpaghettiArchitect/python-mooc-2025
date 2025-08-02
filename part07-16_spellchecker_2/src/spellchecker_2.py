from difflib import get_close_matches


def main() -> None:
    if True:
        text = input("Write text: ")
    else:
        text = "This is acually a good and usefull program"

    dictionary = load_dictionary("wordlist.txt")

    corrections, errors = check_spelling(text, dictionary)

    suggestions = get_suggestions(errors, dictionary)

    print(corrections)
    print(suggestions)


def load_dictionary(filename: str) -> list:
    dictionary = []
    with open(filename) as words_file:
        for word in words_file:
            word = word.strip()
            dictionary.append(word)
    return dictionary


def check_spelling(text: str, dictionary: list) -> tuple[str, list[str]]:
    words = text.split(" ")
    result = ""
    wrong_words = []
    for word in words:
        if word.lower() not in dictionary:
            result += f"*{word}* "
            wrong_words.append(word)
        else:
            result += f"{word} "

    return result.strip(), wrong_words


def get_suggestions(wrong_words: list[str], dictionary: list[str]) -> str:
    if len(wrong_words) != 0:
        suggestions = "suggestions:\n"
    else:
        return ""

    for word in wrong_words:
        close_matches = get_close_matches(word, dictionary)
        suggestions += f"{word}: {', '.join(close_matches)}\n"

    return suggestions.strip()


main()
