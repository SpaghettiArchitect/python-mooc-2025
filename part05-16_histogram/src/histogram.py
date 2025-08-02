def histogram(string: str) -> None:
    repetitions = {}
    for char in string:
        if char not in repetitions:
            repetitions[char] = 0
        repetitions[char] += 1
    for letter in repetitions:
        print(f"{letter} {"*" * repetitions[letter]}")


if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")
