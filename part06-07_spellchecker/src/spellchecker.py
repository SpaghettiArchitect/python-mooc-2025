def main() -> None:
    if True:
        text = input("Write text: ")
    else:
        text = "This is acually a good and usefull program"

    dictionary = []
    with open("wordlist.txt") as words_file:
        for word in words_file:
            word = word.strip()
            dictionary.append(word)

    words = text.split(" ")
    result = ""
    for word in words:
        if word.lower() not in dictionary:
            result += f"*{word}* "
        else:
            result += f"{word} "

    print(result.strip())


main()
