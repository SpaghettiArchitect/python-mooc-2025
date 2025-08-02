from random import sample


def main() -> None:
    word_list = words(3, "ca")
    for word in word_list:
        print(word)


def words(n: int, beginning: str) -> list[str]:
    dictionary = load_all_words("words.txt")
    found = []

    for word in dictionary:
        if word.startswith(beginning) and word not in found:
            found.append(word)

    if len(found) < n:
        raise ValueError("not enough words beginning with the specified string")

    return sample(found, n)


def load_all_words(filename: str) -> list[str]:
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line.strip())
    return result


# main()
