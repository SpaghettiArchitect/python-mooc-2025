def main() -> None:
    filename = "dictionary.txt"
    dictionary = load_dictionary(filename)

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        command = int(input("Function: "))

        if command == 1:
            word_finnish = input("The word in Finnish: ")
            word_english = input("The word in English: ")
            add_to_dictionary(filename, dictionary, word_finnish, word_english)
            print("Dictionary entry added")

        elif command == 2:
            search_term = input("Search term: ")
            found_terms = search_dictionary(dictionary, search_term)
            for finnish, english in found_terms.items():
                print(f"{finnish} - {english}")

        elif command == 3:
            print("Bye!")
            break


def search_dictionary(dictionary: dict, search_term: str) -> dict:
    results = {}
    for finnish, english in dictionary.items():
        if search_term in finnish or search_term in english:
            results[finnish] = english

    return results


def add_to_dictionary(filename: str, dictionary: dict, finnish: str, english: str):
    with open(filename, "a") as file:
        file.write(f"{finnish};{english}\n")

    dictionary[finnish] = english


def load_dictionary(filename: str) -> dict[str, str]:
    dictionary = {}
    with open(filename) as file:
        for line in file:
            finnish, english = line.strip().split(";")
            dictionary[finnish] = english

    return dictionary


main()
