def longest(strings: list[str]) -> str:
    long_str = ""
    for string in strings:
        if len(string) > len(long_str):
            long_str = string

    return long_str


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
