def invert(dictionary: dict) -> None:
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[value] = key

    for value, key in new_dictionary.items():
        dictionary.pop(key)
        dictionary[value] = key


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
