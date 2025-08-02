from string import punctuation


def most_common_words(filename: str, lower_limit: int):
    total_occurrences = {}
    with open(filename) as file:
        for line in file:

            new_line = "".join(
                [char for char in line.strip() if char not in punctuation]
            )

            for word in new_line.split():
                if word not in total_occurrences:
                    total_occurrences[word] = 0
                total_occurrences[word] += 1

    return {
        word: occurrences
        for word, occurrences in total_occurrences.items()
        if occurrences >= lower_limit
    }


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
